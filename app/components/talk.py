import reflex as rx

from app.components.appearance import appearance_page, appearance_toggle
from app.components.welcome import brand, safety
from app.components.portrait_motion import portrait_motion
from app.states.talk_state import TalkState


def talk_header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            brand(),
            rx.el.div(
                appearance_toggle(),
                rx.el.a(
                    rx.icon(
                        "arrow-left", class_name="h-4 w-4", aria_hidden=True
                    ),
                    "Back to welcome",
                    href="/",
                    class_name="inline-flex items-center gap-2 rounded-sm text-sm text-[var(--mira-muted)] hover:text-[var(--mira-foreground)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--mira-focus)]",
                ),
                class_name="flex flex-wrap items-center justify-end gap-3 sm:gap-6",
            ),
            class_name="mx-auto flex w-full max-w-[1200px] items-center justify-between gap-4 px-6 py-6 md:px-10",
        ),
        class_name="border-b border-[var(--mira-border)]/10 bg-[var(--mira-canvas)]",
    )


def companion_profile() -> rx.Component:
    return rx.el.section(
        portrait_motion(TalkState.processing),
        rx.el.div(
            rx.el.p(
                "YOUR AI COMPANION",
                class_name="text-[10px] font-medium tracking-[0.18em] text-[var(--mira-muted)]",
            ),
            rx.el.h2(
                "Meet Mira.",
                class_name="mt-3 font-['DM_Serif_Display'] text-3xl text-[var(--mira-foreground)] lg:text-4xl",
            ),
            rx.el.p(
                "A little space to pause, put a feeling into words, and reflect at your pace.",
                class_name="mt-3 text-sm leading-7 text-[var(--mira-muted)]",
            ),
            rx.el.p(
                "Fictional AI · Not a real person",
                class_name="mt-4 text-xs font-medium text-[var(--mira-accent-text)]",
            ),
            class_name="lg:mt-7",
        ),
        aria_label="About your companion",
        class_name="flex items-center gap-5 lg:sticky lg:top-8 lg:block",
    )


def connection_notice() -> rx.Component:
    return rx.el.div(
        rx.icon(
            "info",
            class_name="mt-0.5 h-4 w-4 shrink-0 text-[var(--mira-accent-text)]",
            aria_hidden=True,
        ),
        rx.el.div(
            rx.el.p(
                rx.cond(
                    TalkState.connected,
                    "AI connection configured",
                    "AI replies unavailable until connected",
                ),
                class_name="text-sm font-medium text-[var(--mira-foreground)]",
            ),
            rx.el.p(
                rx.cond(
                    TalkState.connected,
                    "Sending shares this conversation with OpenAI to generate a reply. Service availability may vary. AI can get things wrong.",
                    "You can explore the prompts and write a message, but Mira cannot reply yet. Sending will show an error; no AI request will be made.",
                ),
                class_name="mt-1 text-xs leading-6 text-[var(--mira-muted)]",
            ),
        ),
        role="status",
        class_name="flex gap-2.5 border-b border-[var(--mira-border)]/10 bg-[var(--mira-notice)] px-4 py-3 sm:px-5",
    )


def starter_prompt(prompt: str) -> rx.Component:
    return rx.el.button(
        prompt,
        rx.icon(
            "arrow-up-right",
            class_name="h-4 w-4 shrink-0 text-[var(--mira-accent-text)]",
            aria_hidden=True,
        ),
        type="button",
        on_click=lambda: TalkState.choose_prompt(prompt),
        disabled=TalkState.processing,
        class_name="flex w-full items-center justify-between gap-3 rounded-2xl border border-[var(--mira-sage)]/40 bg-[var(--mira-canvas)] px-4 py-3 text-left text-sm text-[var(--mira-muted)] transition-colors hover:bg-[var(--mira-surface)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--mira-focus)] disabled:cursor-not-allowed disabled:opacity-60",
    )


def empty_thread() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                "sprout",
                class_name="h-6 w-6 text-[var(--mira-leaf)]",
                aria_hidden=True,
            ),
            class_name="mb-5 flex h-12 w-12 items-center justify-center rounded-full bg-[var(--mira-sage)]/20",
        ),
        rx.el.h3(
            "Begin wherever you are.",
            class_name="font-['DM_Serif_Display'] text-3xl text-[var(--mira-foreground)]",
        ),
        rx.el.p(
            "There’s no right thing to say. Choose a starting thought below, or write something of your own.",
            class_name="mt-3 max-w-[460px] text-sm leading-7 text-[var(--mira-muted)]",
        ),
        rx.el.p(
            "STARTING THOUGHTS · SELECT TO EDIT",
            class_name="mb-3 mt-7 text-[10px] font-medium tracking-[0.14em] text-[var(--mira-muted)]",
        ),
        rx.el.div(
            rx.foreach(TalkState.starter_prompts, starter_prompt),
            class_name="flex w-full max-w-[460px] flex-col gap-2.5",
        ),
        class_name="mx-auto flex w-full max-w-[460px] flex-col items-start justify-center rounded-2xl border border-[var(--mira-sage)]/20 bg-[var(--mira-card)]/95 p-5 sm:p-7",
    )


def message_bubble(message: dict[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                rx.cond(message["role"] == "user", "You", "Mira · AI"),
                class_name="mb-1 text-[11px] font-semibold text-[var(--mira-leaf)]",
            ),
            rx.el.p(
                message["content"],
                class_name="whitespace-pre-wrap text-sm leading-6 [overflow-wrap:anywhere]",
            ),
            class_name=rx.cond(
                message["role"] == "user",
                "relative max-w-[90%] rounded-xl rounded-tr-none border border-[var(--mira-sage)]/25 bg-[var(--mira-surface)] px-4 py-2.5 text-[var(--mira-foreground)] before:absolute before:-right-[7px] before:top-0 before:h-2 before:w-2 before:bg-[var(--mira-surface)] before:[clip-path:polygon(0_0,100%_0,0_100%)] sm:max-w-[82%]",
                "relative max-w-[90%] rounded-xl rounded-tl-none border border-[var(--mira-sage)]/20 bg-[var(--mira-card)] px-4 py-2.5 text-[var(--mira-foreground)] before:absolute before:-left-[7px] before:top-0 before:h-2 before:w-2 before:bg-[var(--mira-card)] before:[clip-path:polygon(0_0,100%_0,100%_100%)] sm:max-w-[82%]",
            ),
        ),
        key=message["id"],
        class_name=rx.cond(
            message["role"] == "user",
            "flex w-full justify-end",
            "flex w-full justify-start",
        ),
    )


def composer() -> rx.Component:
    return rx.el.div(
        rx.el.form(
            rx.el.label(
                "What’s on your mind?",
                html_for="mira-message",
                class_name="sr-only text-[var(--mira-foreground)]",
            ),
            rx.el.div(
                rx.el.textarea(
                    id="mira-message",
                    name="message",
                    default_value=TalkState.draft,
                    key=TalkState.composer_version,
                    placeholder="Start with a thought or a feeling…",
                    rows=2,
                    max_length=4000,
                    disabled=TalkState.processing,
                    aria_describedby="composer-help composer-error",
                    aria_invalid=TalkState.error != "",
                    class_name="block min-h-12 max-h-36 w-full min-w-0 flex-1 resize-y rounded-2xl bg-[var(--mira-canvas)] px-4 py-3 text-base leading-6 text-[var(--mira-foreground)] placeholder:text-[var(--mira-muted)]/80 focus:outline-hidden disabled:cursor-wait disabled:opacity-70",
                ),
                rx.el.button(
                    rx.cond(
                        TalkState.processing,
                        rx.icon(
                            "loader-circle",
                            class_name="h-4 w-4 animate-spin",
                            aria_hidden=True,
                        ),
                        rx.icon("send", class_name="h-4 w-4", aria_hidden=True),
                    ),
                    rx.cond(TalkState.processing, "Sending…", "Send"),
                    type="submit",
                    disabled=TalkState.processing,
                    class_name="mb-1 mr-1 inline-flex min-h-11 shrink-0 items-center justify-center gap-2 rounded-full bg-[var(--mira-primary)] px-4 py-3 text-xs font-medium text-[var(--mira-primary-text)] hover:bg-[var(--mira-primary-hover)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--mira-focus)] disabled:cursor-wait disabled:opacity-60",
                ),
                class_name="flex items-end gap-1 rounded-[24px] border border-[var(--mira-sage)]/40 bg-[var(--mira-canvas)] p-1 focus-within:border-[var(--mira-focus)] focus-within:ring-1 focus-within:ring-[var(--mira-focus)]",
            ),
            rx.el.p(
                "Up to 4,000 characters. Share only what feels comfortable.",
                id="composer-help",
                class_name="mt-2 text-[11px] leading-5 text-[var(--mira-muted)]",
            ),
            on_submit=TalkState.submit_message,
            reset_on_submit=False,
        ),
        rx.el.div(
            rx.cond(
                TalkState.error != "",
                rx.el.p(
                    TalkState.error,
                    role="alert",
                    class_name="mt-3 rounded-xl border border-[var(--mira-accent)]/40 bg-[var(--mira-notice)] p-3 text-xs leading-5 text-[var(--mira-accent-text)]",
                ),
            ),
            id="composer-error",
        ),
        rx.el.p(
            "Session only: this app does not save your conversation to a database. New conversation clears this session’s thread. When connected, messages are sent to OpenAI; avoid identifying or sensitive details.",
            class_name="mt-2 text-[11px] leading-5 text-[var(--mira-muted)]",
        ),
        class_name="shrink-0 border-t border-[var(--mira-border)]/10 bg-[var(--mira-card)] p-3 sm:p-4",
    )


def conversation() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src="/portrait_warm_soft.png",
                    alt="",
                    aria_hidden=True,
                    class_name="h-11 w-11 shrink-0 rounded-full bg-[var(--mira-portrait-surface)] object-cover object-[50%_30%]",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Mira",
                        id="conversation-heading",
                        tab_index=-1,
                        class_name="font-['DM_Serif_Display'] text-2xl leading-7 text-[var(--mira-foreground)]",
                    ),
                    rx.el.p(
                        "AI companion · Fictional, not a person",
                        class_name="text-[11px] leading-5 text-[var(--mira-muted)]",
                    ),
                ),
                class_name="flex min-w-0 items-center gap-3",
            ),
            rx.el.button(
                rx.icon("rotate-ccw", class_name="h-4 w-4", aria_hidden=True),
                "New conversation",
                type="button",
                on_click=TalkState.new_conversation,
                disabled=TalkState.processing,
                class_name="inline-flex min-h-11 shrink-0 items-center gap-2 rounded-full border border-[var(--mira-sage)]/40 bg-[var(--mira-card)] px-3 py-2 text-[11px] text-[var(--mira-muted)] hover:bg-[var(--mira-surface)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--mira-focus)] disabled:cursor-not-allowed disabled:opacity-50",
            ),
            class_name="flex shrink-0 flex-wrap items-center justify-between gap-3 border-b border-[var(--mira-border)]/10 bg-[var(--mira-surface)] px-4 py-3 sm:px-5",
        ),
        rx.el.div(connection_notice(), class_name="shrink-0"),
        rx.el.div(
            rx.cond(
                TalkState.messages.length() == 0,
                empty_thread(),
                rx.el.div(
                    rx.foreach(TalkState.messages, message_bubble),
                    class_name="flex flex-col gap-3 py-1",
                ),
            ),
            rx.cond(
                TalkState.processing,
                rx.el.p(
                    rx.icon(
                        "loader-circle",
                        class_name="h-4 w-4 animate-spin",
                        aria_hidden=True,
                    ),
                    "Waiting for Mira’s AI reply…",
                    role="status",
                    class_name="mt-3 flex w-fit items-center gap-2 rounded-xl rounded-tl-none border border-[var(--mira-sage)]/20 bg-[var(--mira-card)] px-4 py-3 text-xs text-[var(--mira-muted)]",
                ),
            ),
            role="log",
            aria_label="Conversation messages",
            aria_live="polite",
            aria_relevant="additions text",
            aria_busy=TalkState.processing,
            tab_index=0,
            class_name="min-h-0 flex-1 overflow-y-auto overscroll-contain bg-[var(--mira-canvas)] p-4 [background-image:radial-gradient(circle_at_1px_1px,var(--mira-sage)_0.65px,transparent_0.8px)] [background-size:26px_26px] focus-visible:outline-2 focus-visible:outline-offset-[-2px] focus-visible:outline-[var(--mira-sage)] sm:p-6",
        ),
        composer(),
        aria_labelledby="conversation-heading",
        class_name="mira-chat flex h-[760px] max-h-[1000px] min-h-[680px] w-full min-w-0 flex-col overflow-hidden rounded-[24px] border border-[var(--mira-sage)]/40 bg-[var(--mira-card)] sm:h-[780px] lg:h-[min(850px,90dvh)]",
    )


def talk() -> rx.Component:
    return appearance_page(
        rx.el.div(
            rx.el.a(
                "Skip to conversation",
                href="#conversation-heading",
                class_name="sr-only z-50 rounded-full bg-[var(--mira-primary)] px-5 py-3 text-[var(--mira-primary-text)] focus:not-sr-only focus:absolute focus:left-4 focus:top-4",
            ),
            talk_header(),
            rx.el.main(
                rx.el.div(
                    rx.el.p(
                        "A LITTLE SPACE FOR YOU",
                        class_name="text-[11px] font-medium tracking-[0.18em] text-[var(--mira-muted)]",
                    ),
                    rx.el.h1(
                        "Let’s make room for what’s here.",
                        class_name="mt-4 font-['DM_Serif_Display'] text-4xl leading-tight text-[var(--mira-foreground)] md:text-5xl",
                    ),
                    rx.el.p(
                        "Mira is not a clinician, therapy, or an emergency service. If you’re in danger, call your local emergency number now. Don’t wait for an AI reply.",
                        class_name="mt-5 max-w-[850px] text-sm leading-7 text-[var(--mira-muted)]",
                    ),
                    rx.el.a(
                        "Crisis support & safety resources",
                        rx.icon(
                            "arrow-down",
                            class_name="h-3.5 w-3.5",
                            aria_hidden=True,
                        ),
                        href="#safety",
                        class_name="mt-3 inline-flex items-center gap-2 rounded-sm text-sm font-medium text-[var(--mira-accent-text)] underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--mira-focus)]",
                    ),
                    class_name="mb-7",
                ),
                rx.el.div(
                    companion_profile(),
                    conversation(),
                    class_name="grid w-full items-start gap-6 lg:grid-cols-[280px_minmax(0,1fr)] lg:gap-10",
                ),
                class_name="mx-auto w-full max-w-[1200px] px-6 pb-12 pt-10 md:px-10 md:pb-16 md:pt-12",
            ),
            safety(),
            class_name="min-h-dvh bg-[var(--mira-canvas)] font-['DM_Sans'] text-[var(--mira-foreground)] selection:bg-[var(--mira-sage)]/40",
        )
    )
