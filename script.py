class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return "{name}. \"{title}\". {year}, {medium}. {names}, {location}.".format(name = self.artist, title = self.title, year = self.year, medium = self.medium, names = self.owner.name, location = self.owner.location)

class Marketplace:
  def __init__(self):
    self.listings = []
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, remove_listing):
    self.listings.remove(remove_listing)

  def show_listings(self):
    for listing in self.listings:
      return listing

class Client:
  
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = "Private Collection"
  
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)


class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return "{}, {}".format(self.art.title , self.price)


veneer = Marketplace()

edytta = Client("Edytta Halpirt", None, False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')

print(veneer.show_listings())

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)

print(veneer.show_listings())

