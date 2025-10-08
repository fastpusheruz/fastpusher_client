from fastpusher.pusher import FastPusher

pusher = FastPusher(
    url="http://127.0.0.1:8000",
    token="OFJd0rU2J0iqFsPerLZNnmHpP9d7Fsm34fB1I74hHu0"
)


def push_message():
    pusher.push(
        channel="admin",
        data={
            "title": "Hello World!",
            "body": "This is a test message."
        }
    )


if __name__ == "__main__":
    push_message()
