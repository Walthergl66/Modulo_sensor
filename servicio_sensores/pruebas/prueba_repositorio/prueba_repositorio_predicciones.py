import pytest
from dominio.ubicacion import Ubicacion
from dominio.prediccion_sequia import PrediccionSequia
from app.esquemas.esquema_prediccion import PrediccionCrear  # Ajusta el import según tu proyecto
from app.repositorios import repositorio_predicciones  # Ajusta el import

def test_crear_prediccion(db_session):
    # Crear ubicación para la predicción
    ubicacion = Ubicacion(
        latitud="10.123",
        longitud="-70.456",
        descripcion="Lugar de prueba"
    )
    db_session.add(ubicacion)
    db_session.commit()

    prediccion_data = PrediccionCrear(
        ubicacion_id=ubicacion.id,
        probabilidad=0.8,
        comentario="Test de predicción"
    )
    prediccion = repositorio_predicciones.crear_prediccion(db_session, prediccion_data)
    assert prediccion.id is not None
    assert prediccion.probabilidad == 0.8
    assert prediccion.comentario == "Test de predicción"
    assert prediccion.ubicacion_id == ubicacion.id


def test_obtener_predicciones(db_session):
    # Crear ubicación
    ubicacion = Ubicacion(
        latitud="10.123",
        longitud="-70.456",
        descripcion="Lugar de prueba"
    )
    db_session.add(ubicacion)
    db_session.commit()

    # Crear predicción para esa ubicación
    prediccion_data = PrediccionCrear(
        ubicacion_id=ubicacion.id,
        probabilidad=0.6,
        comentario="Otra prueba"
    )
    prediccion_creada = repositorio_predicciones.crear_prediccion(db_session, prediccion_data)

    # Obtener predicciones para la ubicación
    predicciones = repositorio_predicciones.obtener_predicciones_por_ubicacion(db_session, ubicacion.id)

    assert len(predicciones) >= 1
    assert any(p.id == prediccion_creada.id for p in predicciones)
