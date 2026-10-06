import reflex as rx
from reflex.style import toggle_color_mode


def appearance_toggle() -> rx.Component:
    return rx.el.button(
        rx.color_mode_cond(
            light=rx.icon(
                "moon", class_name="h-4 w-4 shrink-0", aria_hidden=True
            ),
            dark=rx.icon(
                "sun", class_name="h-4 w-4 shrink-0", aria_hidden=True
            ),
        ),
        rx.color_mode_cond(light="Dark mode", dark="Light mode"),
        type="button",
        on_click=toggle_color_mode,
        aria_label=rx.color_mode_cond(
            light="Appearance: light. Switch to dark mode",
            dark="Appearance: dark. Switch to light mode",
        ),
        title=rx.color_mode_cond(
            light="Switch to dark mode", dark="Switch to light mode"
        ),
        class_name="inline-flex min-h-11 shrink-0 items-center justify-center gap-2 rounded-full border border-[var(--mira-sage)]/50 bg-[var(--mira-card)] px-3 py-2 text-xs font-medium text-[var(--mira-foreground)] transition-colors hover:bg-[var(--mira-surface)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--mira-focus)] sm:px-4 sm:text-sm",
    )


def appearance_page(content: rx.Component) -> rx.Component:
    return rx.el.div(
        content,
        class_name=rx.color_mode_cond(
            light="min-h-dvh bg-[var(--mira-canvas)] text-[var(--mira-foreground)] [color-scheme:light] [--mira-canvas:#F7F5EE] [--mira-foreground:#263D36] [--mira-muted:#52645A] [--mira-primary:#263D36] [--mira-primary-text:#F7F5EE] [--mira-primary-hover:#40584D] [--mira-focus:#263D36] [--mira-sage:#98AA98] [--mira-border:#263D36] [--mira-card:#FAF9F4] [--mira-surface:#E9EDE3] [--mira-brand-surface:#EEF0E7] [--mira-portrait-surface:#E6E8DC] [--mira-accent:#C98871] [--mira-accent-text:#765041] [--mira-editorial-accent:#8A5A47] [--mira-accent-surface:#EEDDD3] [--mira-notice:#F3EDE5] [--mira-leaf:#526B58] [--mira-leaf-soft:#718770]",
            dark="min-h-dvh bg-[var(--mira-canvas)] text-[var(--mira-foreground)] [color-scheme:dark] [--mira-canvas:#182722] [--mira-foreground:#EBEEE4] [--mira-muted:#BBC9BB] [--mira-primary:#B4C8AF] [--mira-primary-text:#182722] [--mira-primary-hover:#CCDCC5] [--mira-focus:#D9B19A] [--mira-sage:#A5BBA6] [--mira-border:#C4D5C3] [--mira-card:#24372E] [--mira-surface:#2E4337] [--mira-brand-surface:#2E4337] [--mira-portrait-surface:#34473B] [--mira-accent:#D9A38A] [--mira-accent-text:#E8B9A0] [--mira-editorial-accent:#E8B9A0] [--mira-accent-surface:#503C32] [--mira-notice:#352F29] [--mira-leaf:#B4CCAD] [--mira-leaf-soft:#A5BBA6]",
        ),
    )
