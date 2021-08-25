import subprocess
import fire

def convert(input, output):
  command = f'ffmpeg -i {input} -ab 160k -ac 2 -ar 44100 -vn {output}'
  subprocess.call(command, shell=True)

if __name__ == '__main__':
  fire.Fire(convert)
