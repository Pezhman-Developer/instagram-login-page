import flet as ft
from flet import Icons, colors
import webbrowser  

class InstagramLogin:
    def __init__(self):
        self.users = {}

    def main(self, page: ft.Page):
        page.title = "MOMENTIFY"
        page.window_width = 400
        page.window_height = 700
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "light"
        page.bgcolor = "#FAFAFA"


        def open_facebook(e):
            webbrowser.open("https://www.facebook.com/login/")


        def show_login_page():
            page.clean()
            page.add(
                ft.Column(
                    [
                        login_container,
                        signup_section,
                        get_app_section,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                )
            )

        def show_signup_page(e):
            page.clean()
            page.add(
                ft.Column(
                    [
                        signup_container,
                        login_section,
                        get_app_section,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                )
            )

        def handle_login(e):
            username = username_field.value
            password = password_field.value
            
            if username and password:
                if username in self.users and self.users[username] == password:
                    message.value = "Login successful!"
                    message.color = "green"
                else:
                    message.value = "Invalid credentials"
                    message.color = "red"
            else:
                message.value = "Please fill all fields"
                message.color = "red"
            page.update()

        def handle_register(e):
            email = email_field.value
            fullname = fullname_field.value
            username = signup_username_field.value
            password = signup_password_field.value
            
            if email and fullname and username and password:
                if username not in self.users:
                    self.users[username] = password
                    signup_message.value = "Registration successful! Please login."
                    signup_message.color = "green"
                    email_field.value = ""
                    fullname_field.value = ""
                    signup_username_field.value = ""
                    signup_password_field.value = ""
                    page.update()
                    show_login_page()
                else:
                    signup_message.value = "Username already exists"
                    signup_message.color = "red"
            else:
                signup_message.value = "Please fill all fields"
                signup_message.color = "red"
            page.update()

        def toggle_password_visibility(e, field):
            field.password = not field.password
            page.update()

      
        username_field = ft.TextField(
            label="Phone number, username, or email",
            width=300,
            height=45,
        )

        password_field = ft.TextField(
            label="Password",
            password=True,
            width=300,
            height=45,
            suffix=ft.IconButton(
                icon=Icons.VISIBILITY_OFF,
                on_click=lambda e: toggle_password_visibility(e, password_field),
            ),
        )

       
        email_field = ft.TextField(
            label="Email",
            width=300,
            height=45,
        )

        fullname_field = ft.TextField(
            label="Full Name",
            width=300,
            height=45,
        )

        signup_username_field = ft.TextField(
            label="Username",
            width=300,
            height=45,
        )

        signup_password_field = ft.TextField(
            label="Password",
            password=True,
            width=300,
            height=45,
            suffix=ft.IconButton(
                icon=Icons.VISIBILITY_OFF,
                on_click=lambda e: toggle_password_visibility(e, signup_password_field),
            ),
        )

        
        message = ft.Text(
            size=14,
            text_align=ft.TextAlign.CENTER,
        )

        signup_message = ft.Text(
            size=14,
            text_align=ft.TextAlign.CENTER,
        )

       
        login_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Momentify", size=30, weight=ft.FontWeight.BOLD),
                    username_field,
                    password_field,
                    ft.ElevatedButton(
                        "Log in",
                        width=300,
                        height=45,
                        on_click=handle_login,
                    ),
                    ft.Row(
                        [
                            ft.Container(content=ft.Divider(), expand=True),
                            ft.Text("OR", size=12),
                            ft.Container(content=ft.Divider(), expand=True),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.TextButton(  
                        content=ft.Row(
                            [
                                ft.Icon(name=Icons.FACEBOOK),
                                ft.Text(
                                    "Log in with Facebook",
                                    size=14,
                                    weight=ft.FontWeight.W_600,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        on_click=open_facebook, 
                    ),
                    ft.TextButton(text="Forgot password?"),
                    message,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=40,
            width=400,
        )


        signup_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Momentify", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Sign up to see photos and videos from your friends.", 
                           size=14, 
                           text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton(  
                        content=ft.Row(
                            [
                                ft.Icon(name=Icons.FACEBOOK, color=ft.colors.WHITE),
                                ft.Text("Log in with Facebook"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        width=300,
                        bgcolor=ft.colors.BLUE,
                        on_click=open_facebook,  
                    ),
                    ft.Row(
                        [
                            ft.Container(content=ft.Divider(), expand=True),
                            ft.Text("OR", size=12),
                            ft.Container(content=ft.Divider(), expand=True),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    email_field,
                    fullname_field,
                    signup_username_field,
                    signup_password_field,
                    ft.ElevatedButton(
                        "Sign up",
                        width=300,
                        height=45,
                        on_click=handle_register,
                    ),
                    signup_message,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=40,
            width=400,
        )


        signup_section = ft.Container(
            content=ft.Row(
                [
                    ft.Text("Don't have an account?"),
                    ft.TextButton(
                        "Sign up",
                        on_click=show_signup_page,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=10,
            width=400,
        )


        login_section = ft.Container(
            content=ft.Row(
                [
                    ft.Text("Have an account?"),
                    ft.TextButton(
                        "Log in",
                        on_click=lambda _: show_login_page(),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=10,
            width=400,
        )
        def open_app_store(e):
            webbrowser.open("https://apps.apple.com/us/app/instagram/id389801252")
        def open_google_play(e):
            webbrowser.open("https://play.google.com/store/apps/details?id=com.instagram.android")


        get_app_section = ft.Column(
            
            [
                ft.Text("Get the app."),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.TextButton("App Store",on_click=open_app_store),
                            width=136,
                            height=40,
                            bgcolor=ft.colors.BLACK,
                            border_radius=10,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.TextButton("Google Play",on_click=open_google_play),
                            width=136,
                            height=40,
                            bgcolor=ft.colors.BLACK,
                            border_radius=10,
                            alignment=ft.alignment.center,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )


        show_login_page()

if __name__ == "__main__":
    instagram_login = InstagramLogin()
    ft.app(target=instagram_login.main)
