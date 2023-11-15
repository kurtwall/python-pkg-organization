import gzip

from demo_reader.util import writer

opener = gz.open

if __name__ == "__main__":
    writer.main(opener)
