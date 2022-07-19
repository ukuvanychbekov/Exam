from flask_wtf import FlaskForm
import wtforms as wf
from wtforms import validators



class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired(), validators.Length(min=8, max=10)])
    submit = wf.SubmitField('OK')




class EmployeeForm(FlaskForm):
    fullname = wf.StringField('ФИО', validators=[wf.validators.DataRequired()])
    phone = wf.StringField('Номер телефона', validators=[wf.validators.DataRequired()])
    short_info = wf.TextAreaField('Краткая информация', validators=[wf.validators.DataRequired()])
    experience = wf.IntegerField('Опыт работы', validators=[wf.validators.DataRequired()])
    preferred_position = wf.StringField('Предпочитаемая должность', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('OK')

    def validate_fullname(self, field):
        dict1 = {'space': 0}
        for i in field.data:
            if i == ' ':
                dict1['space'] += 1
        if dict1['space'] != 2:
            raise validators.ValidationError('Возможно Вы указали не полное ФИО')


