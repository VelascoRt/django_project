# TEST -----------------------
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note

class NoteTests(TestCase):

    def setUp(self):
        # Configurar un usuario de prueba
        self.user = User.objects.create_user(username='admin', password='password123')
        self.client.login(username='admin', password='password123')

    def test_create_note(self):
        response = self.client.post(reverse('notes:create'), {
            'title': 'Nueva Nota',
            'content': 'Contenido de la nueva nota'
        })
        self.assertEqual(response.status_code, 302)  # Redirecciona después de crear
        self.assertTrue(Note.objects.filter(title='Nueva Nota').exists())

    def test_update_note(self):
        """Prueba la actualización de una nota existente"""
        note = Note.objects.create(user=self.user, title='Nota a actualizar', content='Contenido original')
        response = self.client.post(reverse('notes:edit', args=[note.pk]), {
            'title': 'Nota actualizada',
            'content': 'Contenido actualizado'
        })
        self.assertEqual(response.status_code, 302)  # Redirecciona después de editar
        note.refresh_from_db()
        self.assertEqual(note.title, 'Nota actualizada')
        self.assertEqual(note.content, 'Contenido actualizado')

    def test_view_note_detail(self):
        """Prueba la visualización de los detalles de una nota"""
        note = Note.objects.create(user=self.user, title='Nota de prueba', content='Contenido de prueba')
        response = self.client.get(reverse('notes:detail', args=[note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nota de prueba')
        self.assertContains(response, 'Contenido de prueba')

    def test_delete_note(self):
        """Prueba la eliminación de una nota"""
        note = Note.objects.create(user=self.user, title='Nota a eliminar', content='Contenido para eliminar')
        response = self.client.post(reverse('notes:delete', args=[note.pk]))
        self.assertEqual(response.status_code, 302)  # Redirecciona después de eliminar
        self.assertFalse(Note.objects.filter(pk=note.pk).exists())

    def test_list_notes(self):
        """Prueba la carga de la lista de notas"""
        Note.objects.create(user=self.user, title='Nota 1', content='Contenido 1')
        Note.objects.create(user=self.user, title='Nota 2', content='Contenido 2')
        response = self.client.get(reverse('notes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nota 1')
        self.assertContains(response, 'Nota 2')
