import reflex as rx

from app.components.welcome import welcome
from app.components.talk import talk
from app.states.talk_state import TalkState


def index() -> rx.Component:
    return welcome()


app = rx.App(
    theme=rx.theme(appearance="light", default_color_mode="system"),
    head_components=[
        rx.el.link(rel="stylesheet", href="/talk.css"),
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            cross_origin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index,
    route="/",
    title="Mira — A little space for you",
    description="Meet Mira, a fictional AI text companion for reflection and everyday feelings. AI support, not therapy or emergency care.",
)
app.add_page(
    talk,
    route="/talk",
    title="Talk with Mira — One thought at a time",
    description="A session-only text conversation with a fictional AI companion. Not therapy, clinical care, or emergency support.",
    on_load=TalkState.check_connection,
)
