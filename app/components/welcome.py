import reflex as rx

from app.components.appearance import appearance_page, appearance_toggle


def start_link() -> rx.Component:
    return rx.el.a(
        "Start talking",
        rx.icon("arrow-up-right", class_name="h-4 w-4", aria_hidden=True),
        href="/talk",
        class_name="inline-flex items-center justify-center gap-3 rounded-full bg-[var(--mira-primary)] px-7 py-3.5 text-sm font-medium text-[var(--mira-primary-text)] transition-colors hover:bg-[var(--mira-primary-hover)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--mira-focus)]",
    )


def brand() -> rx.Component:
    return rx.el.a(
        rx.el.span(
            rx.icon(
                "sprout",
                class_name="h-6 w-6 text-[var(--mira-foreground)]",
                aria_hidden=True,
            ),
            class_name="flex h-10 w-10 items-center justify-center rounded-full border border-[var(--mira-sage)]/50 bg-[var(--mira-brand-surface)]",
        ),
        rx.el.span(
            "mira",
            class_name="font-['DM_Serif_Display'] text-3xl tracking-tight text-[var(--mira-foreground)]",
        ),
        href="/",
        aria_label="Mira home",
        class_name="inline-flex items-center gap-2.5 rounded-sm focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--mira-focus)]",
    )


def navigation() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            brand(),
            rx.el.nav(
                rx.el.a(
                    "How it works",
                    href="#how-it-works",
                    class_name="hidden text-sm text-[var(--mira-foreground)] transition-colors hover:text-[var(--mira-accent-text)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--mira-focus)] sm:inline",
                ),
                rx.el.a(
                    "A note on safety",
                    href="#safety",
                    class_name="hidden text-sm text-[var(--mira-foreground)] transition-colors hover:text-[var(--mira-accent-text)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--mira-focus)] md:inline",
                ),
                appearance_toggle(),
                start_link(),
                aria_label="Main navigation",
                class_name="flex flex-wrap items-center justify-end gap-3 sm:gap-6 lg:gap-8",
            ),
            class_name="mx-auto flex w-full max-w-[1200px] items-center justify-between gap-4 px-6 py-6 md:px-10 md:py-7",
        ),
        class_name="w-full border-b border-[var(--mira-border)]/10 bg-[var(--mira-canvas)]",
    )


def portrait() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute -right-3 top-8 h-44 w-36 rotate-12 rounded-t-full rounded-b-[45%] border border-[var(--mira-sage)]/50 md:-right-7 md:h-60 md:w-48",
            aria_hidden=True,
        ),
        rx.el.div(
            class_name="absolute -left-5 bottom-16 h-24 w-16 -rotate-25 rounded-t-full rounded-b-full bg-[var(--mira-accent)]/20 md:-left-9 md:h-36 md:w-24",
            aria_hidden=True,
        ),
        rx.el.div(
            rx.el.img(
                src="/portrait_warm_soft.png",
                alt="A warm, softly lit portrait representing Mira, a fictional AI companion",
                class_name="h-full w-full object-cover object-center",
            ),
            class_name="relative mx-auto h-[370px] w-full max-w-[380px] overflow-hidden rounded-t-[180px] rounded-b-[32px] bg-[var(--mira-portrait-surface)] md:h-[470px] md:max-w-[410px]",
        ),
        rx.el.div(
            rx.el.span(
                rx.icon(
                    "sparkles",
                    class_name="h-4 w-4 text-[var(--mira-accent-text)]",
                    aria_hidden=True,
                ),
                class_name="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-[var(--mira-accent-surface)]",
            ),
            rx.el.div(
                rx.el.p(
                    "Hi, I’m Mira.",
                    class_name="font-['DM_Serif_Display'] text-xl text-[var(--mira-foreground)]",
                ),
                rx.el.p(
                    "We can take it one thought at a time.",
                    class_name="mt-1 text-xs leading-relaxed text-[var(--mira-muted)]",
                ),
            ),
            class_name="relative mx-auto -mt-14 flex w-[90%] max-w-[350px] items-center gap-3 rounded-2xl border border-[var(--mira-border)]/10 bg-[var(--mira-card)] p-5",
        ),
        rx.el.p(
            "AN AI COMPANION, WITH A HUMAN TOUCH",
            class_name="mt-5 text-center text-[10px] font-medium tracking-[0.17em] text-[var(--mira-muted)]",
        ),
        class_name="relative mx-auto w-full max-w-[440px] px-5 pt-2 lg:px-0",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    rx.el.span(
                        class_name="h-1.5 w-1.5 rounded-full bg-[var(--mira-accent)]",
                        aria_hidden=True,
                    ),
                    "A LITTLE SPACE FOR YOU",
                    class_name="mb-6 flex items-center gap-2.5 text-[11px] font-medium tracking-[0.2em] text-[var(--mira-muted)]",
                ),
                rx.el.h1(
                    "You don’t have to",
                    rx.el.br(),
                    "find the ",
                    rx.el.span(
                        "right",
                        class_name="italic text-[var(--mira-editorial-accent)]",
                    ),
                    rx.el.br(),
                    "words.",
                    class_name="font-['DM_Serif_Display'] text-[48px] leading-[1.09] tracking-[-0.025em] text-[var(--mira-foreground)] sm:text-[62px] lg:text-[76px]",
                ),
                rx.el.p(
                    "Meet Mira, a fictional AI text companion for the moments you want to pause, untangle a thought, or simply put your feelings into words.",
                    class_name="mt-7 max-w-[430px] text-base leading-[1.8] text-[var(--mira-muted)] md:text-[17px]",
                ),
                rx.el.div(
                    start_link(),
                    rx.el.span(
                        "Come as you are.",
                        class_name="text-sm text-[var(--mira-muted)]",
                    ),
                    class_name="mt-8 flex flex-wrap items-center gap-5",
                ),
                rx.el.p(
                    rx.icon(
                        "info",
                        class_name="h-3.5 w-3.5 shrink-0",
                        aria_hidden=True,
                    ),
                    "AI support, not therapy or emergency care.",
                    class_name="mt-5 flex items-center gap-2 text-xs leading-relaxed text-[var(--mira-muted)]",
                ),
                class_name="relative z-10",
            ),
            portrait(),
            class_name="grid items-center gap-14 lg:grid-cols-[1.15fr_1fr] lg:gap-16",
        ),
        class_name="mx-auto w-full max-w-[1200px] px-6 pb-16 pt-12 md:px-10 md:pb-20 md:pt-16 lg:pb-24 lg:pt-20",
        aria_label="Meet Mira",
    )


def topic(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.icon(
                icon,
                class_name="h-5 w-5 text-[var(--mira-leaf)]",
                aria_hidden=True,
            ),
            class_name="mb-5 flex h-11 w-11 items-center justify-center rounded-full bg-[var(--mira-sage)]/20",
        ),
        rx.el.h3(
            title,
            class_name="font-['DM_Serif_Display'] text-2xl text-[var(--mira-foreground)]",
        ),
        rx.el.p(
            description,
            class_name="mt-3 text-sm leading-7 text-[var(--mira-muted)]",
        ),
        class_name="rounded-[24px] border border-[var(--mira-sage)]/30 bg-[var(--mira-card)] p-6 md:p-7",
    )


def topics() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.p(
                "WHATEVER’S ON YOUR MIND",
                class_name="text-[11px] font-medium tracking-[0.18em] text-[var(--mira-muted)]",
            ),
            rx.el.h2(
                "Big feelings. Small moments. All welcome.",
                class_name="mt-4 font-['DM_Serif_Display'] text-3xl leading-tight text-[var(--mira-foreground)] md:text-[40px]",
            ),
            rx.el.p(
                "There’s no perfect place to begin. Here are a few possibilities.",
                class_name="mt-4 text-sm leading-7 text-[var(--mira-muted)] md:text-base",
            ),
            class_name="mb-8 text-center",
        ),
        rx.el.div(
            topic(
                "cloud-sun",
                "The everyday overwhelm",
                "A busy mind, a difficult day, or the feeling that everything is a little too much.",
            ),
            topic(
                "heart",
                "What’s close to your heart",
                "Relationships, change, loneliness, or feelings you haven’t quite named yet.",
            ),
            topic(
                "sprout",
                "A moment to reflect",
                "Notice what’s on your mind, explore a different perspective, or think about a small next step.",
            ),
            class_name="grid gap-4 md:grid-cols-3 md:gap-5",
        ),
        class_name="mx-auto w-full max-w-[1200px] px-6 pb-16 md:px-10 md:pb-24",
    )


def step(number: str, title: str, description: str) -> rx.Component:
    return rx.el.li(
        rx.el.span(
            number,
            class_name="font-['DM_Serif_Display'] text-3xl text-[var(--mira-editorial-accent)]",
            aria_hidden=True,
        ),
        rx.el.div(
            rx.el.h3(
                title,
                class_name="text-base font-medium text-[var(--mira-foreground)]",
            ),
            rx.el.p(
                description,
                class_name="mt-2 text-sm leading-7 text-[var(--mira-muted)]",
            ),
        ),
        class_name="flex gap-5 border-b border-[var(--mira-border)]/10 py-6 last:border-0 first:pt-0 last:pb-0",
    )


def how_it_works() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "A GENTLE BEGINNING",
                    class_name="text-[11px] font-medium tracking-[0.18em] text-[var(--mira-muted)]",
                ),
                rx.el.h2(
                    "A conversation,\nat your pace.",
                    class_name="mt-4 whitespace-pre-line font-['DM_Serif_Display'] text-4xl leading-[1.18] text-[var(--mira-foreground)] md:text-5xl",
                ),
                rx.el.p(
                    "No agenda to follow. No need to have it all figured out. Just a place to start with what’s here, right now.",
                    class_name="mt-5 max-w-[350px] text-sm leading-7 text-[var(--mira-muted)] md:text-base",
                ),
                rx.el.div(
                    rx.icon(
                        "leaf",
                        class_name="h-10 w-10 -rotate-25 text-[var(--mira-leaf-soft)]",
                        aria_hidden=True,
                    ),
                    class_name="mt-8 hidden md:block",
                ),
            ),
            rx.el.ol(
                step(
                    "01",
                    "Start with what’s on your mind",
                    "Write a little or a lot. Even “I don’t know how I’m feeling” is a place to begin.",
                ),
                step(
                    "02",
                    "Explore it with Mira",
                    "Mira is designed to respond with questions and reflections. It’s AI, not a person, and can get things wrong.",
                ),
                step(
                    "03",
                    "Take what feels useful",
                    "You decide what to share and when to stop. Leave room for support from people you trust, too.",
                ),
                class_name="list-none",
            ),
            class_name="grid gap-10 rounded-[32px] bg-[var(--mira-surface)] p-7 md:grid-cols-2 md:gap-16 md:p-12 lg:p-14",
        ),
        id="how-it-works",
        class_name="mx-auto w-full max-w-[1200px] scroll-mt-8 px-6 pb-16 md:px-10 md:pb-20",
    )


def safety() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "shield",
                    class_name="h-6 w-6 text-[var(--mira-accent-text)]",
                    aria_hidden=True,
                ),
                class_name="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[var(--mira-accent)]/15",
            ),
            rx.el.div(
                rx.el.h2(
                    "A companion, not a substitute for care.",
                    class_name="font-['DM_Serif_Display'] text-2xl text-[var(--mira-foreground)] md:text-3xl",
                ),
                rx.el.p(
                    "Mira is not therapy, a clinician, or an emergency service. It cannot diagnose or treat mental health conditions. AI responses may be inaccurate; for professional support, contact a qualified mental health professional.",
                    class_name="mt-3 text-sm leading-7 text-[var(--mira-muted)]",
                ),
                rx.el.p(
                    "If you’re in immediate danger or may harm yourself or someone else, call your local emergency number now. In the U.S., call or text 988 for crisis support. Elsewhere, find a local helpline below.",
                    class_name="mt-3 text-sm font-medium leading-7 text-[var(--mira-foreground)]",
                ),
                rx.el.div(
                    rx.el.a(
                        "Call 988 (U.S.)",
                        href="tel:988",
                        class_name="inline-flex items-center gap-2 rounded-sm text-sm font-medium text-[var(--mira-accent-text)] underline decoration-[var(--mira-accent)]/60 underline-offset-4 hover:text-[var(--mira-foreground)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--mira-focus)]",
                    ),
                    rx.el.a(
                        "Find a local helpline",
                        rx.icon(
                            "arrow-up-right",
                            class_name="h-4 w-4",
                            aria_hidden=True,
                        ),
                        href="https://findahelpline.com/",
                        target="_blank",
                        rel="noopener noreferrer",
                        aria_label="Find a local helpline, opens in a new tab",
                        class_name="inline-flex items-center gap-1 rounded-sm text-sm font-medium text-[var(--mira-accent-text)] underline decoration-[var(--mira-accent)]/60 underline-offset-4 hover:text-[var(--mira-foreground)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--mira-focus)]",
                    ),
                    class_name="mt-5 flex flex-wrap gap-x-6 gap-y-3",
                ),
            ),
            class_name="flex flex-col gap-5 rounded-3xl border border-[var(--mira-accent)]/30 bg-[var(--mira-notice)] p-6 sm:flex-row md:gap-6 md:p-8",
        ),
        id="safety",
        aria_label="Important safety information",
        class_name="mx-auto w-full max-w-[1200px] scroll-mt-8 px-6 pb-14 md:px-10 md:pb-16",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                brand(),
                rx.el.p(
                    "A little space to feel, reflect, and begin again.",
                    class_name="mt-3 text-xs leading-6 text-[var(--mira-muted)]",
                ),
            ),
            rx.el.div(
                rx.el.p(
                    "Made for the human moments.",
                    class_name="font-['DM_Serif_Display'] text-lg text-[var(--mira-foreground)]",
                ),
                rx.el.p(
                    "Mira is a fictional AI companion, not a real person.",
                    class_name="mt-2 text-xs leading-6 text-[var(--mira-muted)]",
                ),
                class_name="md:text-right",
            ),
            class_name="mx-auto flex w-full max-w-[1200px] flex-col justify-between gap-7 px-6 py-8 md:flex-row md:items-center md:px-10",
        ),
        class_name="border-t border-[var(--mira-border)]/10 bg-[var(--mira-canvas)]",
    )


def welcome() -> rx.Component:
    return appearance_page(
        rx.el.div(
            rx.el.a(
                "Skip to content",
                href="#main-content",
                class_name="sr-only z-50 rounded-full bg-[var(--mira-primary)] px-5 py-3 text-[var(--mira-primary-text)] focus:not-sr-only focus:absolute focus:left-4 focus:top-4",
            ),
            navigation(),
            rx.el.main(
                hero(), topics(), how_it_works(), safety(), id="main-content"
            ),
            footer(),
            class_name="min-h-dvh bg-[var(--mira-canvas)] font-['DM_Sans'] text-[var(--mira-foreground)] selection:bg-[var(--mira-sage)]/40",
        )
    )
