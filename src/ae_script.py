import fire

# Covert JSON file to Adobe After Effect Script
#   { text: 'Hellow video!', inPoint: 2.5, outPoint: 2.7 }
class AeScript:
    SMALL_CONTENT_LENGTH = 2
    JUST_CONTENT_LENGTH = 24
    BIG_CONTENT_LENGTH = 30
    SEPARATION_SEC = 0.3

if __name__ == '__main__':
    fire.Fire(AeScript)
