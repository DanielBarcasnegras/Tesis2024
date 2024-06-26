# Documentación general
- Define ROI (Graphic method).py:	
- Define ROI (Pattern method).py:	
- Trackbar HSV.py: Permite observar en tiempo real las regiones generadas bajo cierto rango de parametros HSV. Sirve para determinar los tonos que se desean detectar.

Los códigos llamados Versión Axx son diferentes iteraciones del código de detección. En éste momento la más actualizada corresponde a la Versión A54, ya que esta usa Watchdog para revisar cambios en los archivos de una carpeta determinada y procede a realizar la extracción de datos, para luego enviar la información a MySQL. Se limita a realizar un conteo de pixeles dentro de un ROI.

Cambios por implementar en Versión A54:
- Cambiar labels de ROI (Regions of interest)
- Cambiar labels/columnas
- Conversión de pixeles a referencia real (cm2 o mm2)
- Segmentación Watershed (Requiere más procesamiento previo de las imágenes para usar párametros universales, que no deban cambiarse por las diferentes condiciones ambientales)

Se descartó temporalmente la generación de contornos debido a conflictos de interferencia entre regiones. Un algoritmo watershed más refinado puede ser una solución ante estos problemas de overlapping, pero al menos por el momento no fue posible lograr un tunning optimo de los párametros.

Cambios pendientes en general:
- Subir versión actualizada del código de procesamiento (Fase 2)
- Guardar las imagenes en el sistema de archivos del sistema y guardar los file paths en MySQL. Facilita el proceso y la visualización en interfaz web. Sugerir estrategia de backup en nube con SD de alto endurance.
- Raw data e insights: Ajustes de interfaz para visualizar los datos de mejor manera
- Insights: Generar y subir gráficas de crecimiento (3 tipos)


