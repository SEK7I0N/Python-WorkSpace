import folium
import pandas

volcanos = pandas.read_csv("Volcanoes.txt", sep=',')
lat = list(volcanos["LAT"])
lon = list(volcanos["LON"])
name = list(volcanos["NAME"])
elev = list(volcanos["ELEV"])

def colorGrade(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"  

map = folium.Map(location = [38 , -101], zoom_start=5, tiles = "Stamen Terrain")

fgVolcanos = folium.FeatureGroup(name="Volcanos")
for lt, ln, nam, el in zip(lat, lon, name, elev):
    fgVolcanos.add_child(folium.CircleMarker(location=[lt,ln], radius=7, popup=str(nam)+": "+str(el)+"m",
    fill_color=colorGrade(el), color="black", fill_opacity="0.7"))

fgPop = folium.FeatureGroup(name="Country Population")
fgPop.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
style_function= lambda x: {"fillColor":"green" if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 100000000 else 'red'
}))

map.add_child(fgVolcanos)
map.add_child(fgPop)
map.add_child(folium.LayerControl())

map.save("Map1.html")