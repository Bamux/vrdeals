"""Get the offers from different date sources."""
import data_sources as ds


def expand_offers(offers, new_offers):
    """Expands the list when new offers are available."""
    if offers and new_offers:
        offers.expand(new_offers)
    elif new_offers:
        offers = new_offers
    return offers


def main():
    offers = ds.alternate.main()
    offers = expand_offers(offers, ds.amazon.main())
    offers = expand_offers(offers, ds.oculus_store.main())
    offers = expand_offers(offers, ds.steam_store.main())

    return offers


if __name__ == "__main__":
    main()
