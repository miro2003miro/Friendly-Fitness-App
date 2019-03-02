from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
#from main import ImageButton
from kivy.app import App
from functools import partial
from specialbuttons import ImageButton, LabelButton
import requests
import kivy.utils
from kivy.graphics import Color, Rectangle


class FriendBanner(FloatLayout):
    def __init__(self, **kwargs):
        super(FriendBanner, self).__init__(**kwargs)
        with self.canvas.before:
            Color(rgba=(kivy.utils.get_color_from_hex("#6C5B7B"))[:3] + [.5])
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)


        # Add the friend's avatar
        # Query firebase and order by my_friend_id equalTo friend_id for this person to get their identifer
        check_req = requests.get('https://friendly-fitness.firebaseio.com/.json?orderBy="my_friend_id"&equalTo='
                                 + kwargs['friend_id'])
        data = check_req.json()
        unique_identifer = data.keys()[0]
        their_avatar = data[unique_identifer]['avatar']
        print(their_avatar)

        image_button = ImageButton(source="icons/avatars/" + their_avatar, size_hint=(.3, 1), pos_hint={"top": 1, "right": 0.4},
                                   on_release=partial(App.get_running_app().load_friend_workout_screen, kwargs['friend_id']))

        # Add the friend's ID
        friend_label = LabelButton(text=kwargs['friend_id'], size_hint=(.6, 1), pos_hint={"top": 1, "right": 1})
        self.add_widget(image_button)
        self.add_widget(friend_label)




    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
