import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Tarea


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def tarea_factory(db):
    def _create(**kwargs):
        defaults = {'titulo': 'Tarea de prueba', 'descripcion': 'Descripcion', 'completada': False}
        defaults.update(kwargs)
        return Tarea.objects.create(**defaults)
    return _create


@pytest.mark.django_db
class TestTareaList:
    def test_listar_tareas_retorna_200(self, client):
        url = reverse('tarea-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_listar_tareas_retorna_lista(self, client, tarea_factory):
        tarea_factory(titulo='Tarea 1')
        tarea_factory(titulo='Tarea 2')
        url = reverse('tarea-list')
        response = client.get(url)
        assert len(response.data) == 2


@pytest.mark.django_db
class TestTareaCreate:
    def test_crear_tarea_retorna_201(self, client):
        url = reverse('tarea-list')
        data = {'titulo': 'Nueva tarea', 'descripcion': 'Detalle', 'completada': False}
        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_crear_tarea_sin_titulo_retorna_400(self, client):
        url = reverse('tarea-list')
        response = client.post(url, {}, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_crear_tarea_persiste_en_db(self, client):
        url = reverse('tarea-list')
        client.post(url, {'titulo': 'Persistida'}, format='json')
        assert Tarea.objects.filter(titulo='Persistida').exists()


@pytest.mark.django_db
class TestTareaDetail:
    def test_obtener_tarea_retorna_200(self, client, tarea_factory):
        tarea = tarea_factory()
        url = reverse('tarea-detail', args=[tarea.pk])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['titulo'] == tarea.titulo

    def test_obtener_tarea_inexistente_retorna_404(self, client):
        url = reverse('tarea-detail', args=[9999])
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_actualizar_tarea(self, client, tarea_factory):
        tarea = tarea_factory()
        url = reverse('tarea-detail', args=[tarea.pk])
        response = client.patch(url, {'completada': True}, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['completada'] is True

    def test_eliminar_tarea_retorna_204(self, client, tarea_factory):
        tarea = tarea_factory()
        url = reverse('tarea-detail', args=[tarea.pk])
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_eliminar_tarea_la_remueve_de_db(self, client, tarea_factory):
        tarea = tarea_factory()
        url = reverse('tarea-detail', args=[tarea.pk])
        client.delete(url)
        assert not Tarea.objects.filter(pk=tarea.pk).exists()


@pytest.mark.django_db
class TestHealthCheck:
    def test_health_retorna_200(self, client):
        url = reverse('health-check')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['status'] == 'ok'
