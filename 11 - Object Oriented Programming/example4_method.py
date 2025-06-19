class Drummer():
    def __init__(self, style, lead_hand, brand):
        self.style = style
        self.lead_hand = lead_hand
        self.brand = brand

    def UrutanPukul(self):
        if self.lead_hand == "leaf":
            print("L! R! L! L!")
        else:
            print("R! L! R! R")

    def introduction(self):
        print("Hello every one, im drummer")
        # TypeError: Drummer.introduction() takes 0 positional arguments but 1 was given , akan muncul error ini jika tidak put self
    
    def drummer_lessons(self, grip):
        if grip == "traditional":
            print("Sure, I can teach you")
        else:
            print("sorry i can only teach traditional grip")
        

yoyo_padi = Drummer("pop","Right","Pearl")
# yoyo_padi.UrutanPukul()
# yoyo_padi.introduction()
# print(yoyo_padi.brand)
# print(yoyo_padi.lead_hand)
# print(yoyo_padi.style)
# print("\n")

# yoyo_padi.drummer_lessons("traditional")

yoyo_padi.drummer_lessons("modern")

        