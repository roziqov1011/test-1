"""Minimal Strands Decider 2B demo."""

from strands_decider import Decider


MODEL_ID = "StrandsAgents/strands-decider-2B-hobson-v21"


def main():
    decider = Decider(MODEL_ID)

    state = "Mijoz 3 kundan beri payout ololmayapti."
    choices = [
        "billing",
        "sales",
        "retail",
    ]

    result = decider.choose(
        state=state,
        choices=choices,
    )

    print("State:", state)
    print("Choices:", choices)
    print("Result:", result)


if __name__ == "__main__":
    main()
