import argparse

DATA_SOURCE_URL = 'https://geo.com/mapdata/'


def main():
    parser = argparse.ArgumentParser(description='Process map data.')
    parser.add_argument('--data-source-url')
    parser.add_argument('--id')
    args = vars(parser.parse_args())

    print(args['data_source_url'])
    print(args['id'])

if __name__ == '__main__':
    main()
