def get_data():
  """Returns the data in XML format."""
  data = {
    name:"Aswin's Good Apps",
    website: "aswinapps.com",
    publisher: "Aswin Arulvel",
    latestapp: "AIstar",
    latestappwebsite: "aistar.aswinapps.com",
    about: "Aswin's Good Apps is a set of free apps that will always be free. Aswin's Good Apps. Free Apps for Real.",
    slogan:"Free apps for real",
    
  }
  return xml.etree.ElementTree.tostring(data, encoding="utf-8")
