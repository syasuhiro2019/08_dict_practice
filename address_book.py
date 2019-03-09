def main():
    address_book = [{"name": "株式会社NEXT REVOLUTION",
                     "location": "岩手県八幡平市大更第35地割62番地",
                     "zipcode": "0287111"},

                    {"name": "ペンションあんとる・ど・めえる",
                     "location": "岩手県八幡平市松尾寄木第１地割６１８−１２",
                     "zipcode": "0287111"},

                    {"name": "なかやま荘",
                     "location": "岩手県八幡平市松尾寄木2-512",
                     "zipcode": "0287302"},
                    ]

    print(address_book[0]['name'])
    print(f"所在地 〒{address_book[0]['zipcode']} 住所 {address_book[0]['location']}")

    print(address_book[1]['name'])
    print(f"所在地 〒{address_book[1]['zipcode']} 住所 {address_book[1]['location']}")

    print(address_book[2]['name'])
    print(f"所在地 〒{address_book[2]['zipcode']} 住所 {address_book[2]['location']}")

    for address in address_book:
        name = address['name']
        location = address['location']
        zipcode = address['zipcode']

        print(name)
        print(f'所在地 〒{zipcode} 住所 {location}')

if __name__ == "__main__":
    main()
