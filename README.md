# Tesis2024
Define ROI (Graphic method).py:
Define ROI (Pattern method).py:
Trackbar HSV.py: Permite observar en tiempo real las regiones generadas bajo cierto rango de parametros HSV. Sirve para determinar los tonos que se desean detectar. 

Los códigos llamados Versión Axx son diferentes iteraciones del código de detección. En éste momento la más actualizada corresponde a la Versión A54, ya que esta usa Watchdog para revisar cambios en los archivos de una carpeta determinada y procede a realizar la extracción de datos, para luego enviar la información a MySQL. Se limita a realizar un conteo de pixeles dentro de un ROI.

Se descartó la generación de contornos debido a conflictos de regiones. Un algoritmo watershed más refinado puede ser una solución ante estos problemas de overlapping, pero al menos por el momento no fue posible lograr un tunning optimo de los parametros.
