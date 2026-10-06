import reflex as rx


def portrait_motion(processing: bool = False) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src="/portrait_warm_soft.png",
            alt="Illustrated portrait of Mira, a fictional AI companion, not a real person",
            class_name="absolute inset-0 h-full w-full object-cover object-center",
        ),
        rx.el.div(
            rx.el.img(
                src="/portrait_warm_soft.png",
                alt="",
                class_name="mira-hair absolute inset-0 h-full w-full object-cover object-center",
            ),
            rx.el.div(
                rx.el.img(
                    src="/portrait_warm_soft.png",
                    alt="",
                    class_name="mira-eyelid-source absolute inset-0 h-full w-full object-cover object-center",
                ),
                class_name="mira-blink absolute inset-0",
            ),
            rx.el.div(
                rx.el.img(
                    src="/portrait_warm_soft.png",
                    alt="",
                    class_name="mira-eyelid-source absolute inset-0 h-full w-full object-cover object-center",
                ),
                class_name="mira-blink mira-blink-right absolute inset-0",
            ),
            rx.el.img(
                src="/portrait_warm_soft.png",
                alt="",
                class_name="mira-mouth absolute inset-0 h-full w-full object-cover object-center",
            ),
            aria_hidden=True,
            class_name="pointer-events-none absolute inset-0",
        ),
        class_name=rx.cond(
            processing,
            "mira-portrait mira-portrait-processing relative aspect-[4/5] w-32 shrink-0 overflow-hidden rounded-t-full rounded-b-2xl bg-[var(--mira-portrait-surface)] sm:w-40 lg:w-full lg:rounded-b-[28px]",
            "mira-portrait relative aspect-[4/5] w-32 shrink-0 overflow-hidden rounded-t-full rounded-b-2xl bg-[var(--mira-portrait-surface)] sm:w-40 lg:w-full lg:rounded-b-[28px]",
        ),
    )
