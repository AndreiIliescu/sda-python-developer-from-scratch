from unittest.mock import patch, MagicMock
from unittest import TestCase

import pytest

from blog import BlogPostHistory


class BlogPostHistoryTests(TestCase):

    def test_change_title(self):
        # mock este un obiect care poate imita/inlocui functionalitatea
        # unei metode
        mock = MagicMock()

        # patch() va inlocui metoda precizata, cu obiectul mock
        # pentru functia inlocuita avem nevoie de locatia ei:
        # exemplu: nume_module.NumeClasa.nume_metoda
        with patch('blog.BlogPostHistory.save', mock):
            # In interiorul blocului de with
            # Functia 'save' va fi imitata de obiectul mock
            post_history = BlogPostHistory('title', 'desc')
            post_history.change_title('new_title')

            assert post_history.get_properties() == ('new_title', 'desc')

    def test_problem_with_file(self):
        # Simulam ca functia imitata va avea o eroare de tip OSError
        mock = MagicMock(side_effect=OSError)

        with patch('blog.BlogPostHistory.save', mock):
            post_history = BlogPostHistory('title', 'desc')

            with pytest.raises(Exception):
                post_history.change_desc('desc2')

    def test_get_properties(self):
        # Functia imitata va returna *mereu* valoare specificata in
        # return_value
        mock = MagicMock(return_value=('my_title', 'my_desc'))

        with patch('blog.BlogPostHistory.get_properties', mock):
            post_history = BlogPostHistory('Blog', 'about food')

            assert post_history.get_properties() == ('my_title', 'my_desc')
