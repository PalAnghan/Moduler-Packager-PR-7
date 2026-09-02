import uuid


def generate_uuid():
    return uuid.uuid4()


if __name__ == "__main__":
    print("=" * 30)
    print("Generate Unique Identifiers")
    print("=" * 30)

    unique_id = generate_uuid()

    print("Generated UUID:", unique_id)

    print("=" * 30)