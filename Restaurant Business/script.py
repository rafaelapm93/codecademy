class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return f"The Menu {self.name} it's serve from {str(self.start_time)} am to {str(self.end_time)} pm"

  def calculate_bill(self, purchased_items):
    sum_ = 0
    for pi in purchased_items:
      sum_ += self.items[pi]
    return sum_


class Franchise:
  def __init__(self, address, menus):
    self.address = address 
    self.menus = menus
  def __repr__(self):
    return f"The Franchise Address is {self.address}" 

  def available_menus(self, time):
    list_menus = []
    for menu in self.menus:
      if menu.start_time <= time and menu.end_time > time:
         list_menus.append(menu)
    return list_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

brunch = Menu(name = 'brunch', 
              items ={
              'pancakes': 7.50,
              'waffles': 9.00,     
              'burger': 11.00,
              'home fries': 4.50,
              'coffee': 1.50,
              'espresso': 3.00,
              'tea': 1.00,
              'mimosa': 10.50,
              'orange juice': 3.50},
              start_time = 11,
              end_time = 16)

early_bird = Menu(name = 'early_bird',
                  items ={
                  'salumeria plate': 8.00,
                  'salad and breadsticks (serves 2, no refills)': 14.00,
                  'pizza with quattro formaggi': 9.00,
                  'duck ragu': 17.50, 
                  'mushroom ravioli (vegan)': 13.50, 
                  'coffee': 1.50, 
                  'espresso': 3.00,
                  }, 
                  start_time = 15,
                  end_time = 18
                  )

dinner = Menu(name = 'dinner',
                  items ={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 
                  start_time = 17,
                  end_time = 23
                  )

kids = Menu(name='kids',
            items = {
            'chicken nuggets': 6.50,
            'fusilli with wild mushrooms': 12.00,
            'apple juice': 3.00
            },
            start_time = 11,
            end_time = 21)
          
print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

flagship_store = Franchise(address = "1232 West End Road",
menus = [brunch, early_bird, dinner, kids])

new_installment = Franchise(address = "12 East Mulberry Street",
menus = [brunch, early_bird, dinner, kids])

print(flagship_store.available_menus(12))


print(flagship_store.available_menus(17))

business = Business(name = "Basta Fazoolin' with my Heart", franchise = [flagship_store , new_installment])

arepas_menu = Menu(name = 'lunch/dinner',
                  items ={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 
                  start_time = 10,
                  end_time = 20
                  )
arepas_place = Franchise(name = "189 Fitzgerald Avenue", menus = [arepas_menu])

arepas_business = Business(name = "Take a' Arepa", franchise = [arepas_place])
