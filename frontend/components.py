from reactpy import component, html, hooks

@component
def PageHome():
    email, set_email = hooks.use_state("")
    cv, set_cv = hooks.use_state(None)

    def fetch_cv():
        set_cv(Curriculum.find_by_email(email))

    return html.div(
        html.h1("Inicio"),
        html.button("Ir al formulario"),
        html.br(),
        html.input({
            "type": "email",
            "name": "gmail",
            "placeholder": "Ingrese su gmail",
            "value": email,
            "on_input": lambda e: set_email(e.target.value)
        }),
        html.button({"on_click": fetch_cv}, "Ingresar con Gmail"),
        PageProfile(cv=cv) if cv else None
    )

@component
def PageForm():
    nombre, set_nombre = hooks.use_state("")
    gmail, set_gmail = hooks.use_state("")

    def submit_form():
        cv = Curriculum(gmail, nombre, "", "")  # Assuming empty experience and skills for now
        cv.save()

    return html.div(
        html.h1("Formulario"),
        html.form(
            html.div(
                html.label("Nombre:"),
                html.input({
                    "type": "text",
                    "name": "nombre",
                    "placeholder": "Ingrese su nombre",
                    "value": nombre,
                    "on_input": lambda e: set_nombre(e.target.value)
                }),
            ),
            html.div(
                html.label("Gmail:"),
                html.input({
                    "type": "email",
                    "name": "gmail",
                    "placeholder": "Ingrese su gmail",
                    "value": gmail,
                    "on_input": lambda e: set_gmail(e.target.value)
                }),
            ),
            html.button({"on_click": submit_form}, "Enviar")
        ),
    )

@component
def PageProfile(cv=None):
    if cv:
        return html.div(
            html.h1("Vista"),
            html.p(f"Nombre: {cv.get('education')}"),  # Assuming name is stored in 'education'
            html.p(f"Gmail: {cv.get('user_email')}")
        )
    return None