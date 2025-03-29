from kivy.uix.settings import text_type

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size =(500,700)

Builder.load_file('kalkulator.kv')

class MyLayout(Widget):

    def clear(self):
       self.ids.calc_input.text='0'

    def button_press(self, button):
        prior=self.ids.calc_input.text
        if 'BŁĄD' in prior:
            prior=''

        if prior =='0':
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{button}'
        else:
            self.ids.calc_input.text=f'{prior}{button}'
    
    def remove(self):
        prior=self.ids.calc_input.text
        prior =prior[:-1]
        self.ids.calc_input.text = prior
        if self.ids.calc_input.text==f'':
            self.ids.calc_input.text=f'{0}'
    
    def pos_neg(self):
        prior=self.ids.calc_input.text
        num_list=prior.split(prior)

        if "-" in prior:
            self.ids.calc_input.text=f'{prior.replace('-','')}'
        else:
            self.ids.calc_input.text=f'-{prior}'
        
    def dot(self):
        prior=self.ids.calc_input.text
        num_list=prior.split('+')
        dev_list=prior.split('/')
        min_list=prior.split('-')
        mul_list=prior.split('*')
        if '+' and '.' not in num_list[-1]:
            prior=f'{prior}.'
            self.ids.calc_input.text=prior
        elif '/' and '.' not in dev_list[-1]:
            prior=f'{prior}.'
            self.ids.calc_input.text=prior
        elif '-' and '.' not in min_list[-1]:
            prior=f'{prior}.'
            self.ids.calc_input.text=prior
        elif '*' and '.' not in mul_list[-1]:
            prior=f'{prior}.'
            self.ids.calc_input.text=prior

        elif '.' in prior:
            prior=f'{prior}0.'
            self.ids.calc_input.text=prior
        else:
            prior=f'{prior}.'
            self.ids.calc_input.text=prior

    def math_sign(self, sign):
        prior=self.ids.calc_input.text
        #num_list=prior.split(sign)
        self.ids.calc_input.text=f"{prior}{sign}"
        '''
        if sign in num_list:
            print('WARUNEK')
        '''
    def equals(self):
        prior=self.ids.calc_input.text
        try:
            answer = round(eval(prior),12)
            self.ids.calc_input.text=str(answer)
        except:
            self.ids.calc_input.text='BŁĄD'
    
    def percent(self):
        prior=self.ids.calc_input.text
        percent=float(prior)/int(100)
        prior=round((percent),12)
        self.ids.calc_input.text=str(prior)

        '''
        if '+' in prior:
            num_list = prior.split('+')
            answer=0.0
            for number in num_list:
                answer = answer+float(number)
            self.ids.calc_input.text=str(answer)
        '''

class KalkulatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__=='__main__':
    KalkulatorApp().run()