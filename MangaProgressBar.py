# Copyright (C) 2012  Dim Birua
"""
MangaProgressBar 0.2
   Скрипт добавления прогресс бара на готовые картинки после Mangle.
Новое в версии 0.2:
-- создание белого фона полной ширины и высоты
   (600,800) - для высоты <= 800
   (824, 1200) - для высоты > 800
-- корректный цвет фона и прогрессбара как для сокращенной палитры, так и полной
-- поддержка файла *.cbz напрямую или 1 файл *.cbz внутри папки
-- файлы не затираются, а создаются копии (папка *_MPB или архив *_MPB.cbz)
-- изменения в gui
"""


import sys
import os
import shutil
import zipfile


from PIL import Image, ImageDraw, ImageFile
from PyQt4 import QtCore, QtGui
from MangaProgressBar_UI import Ui_MangaProgressBar

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_MangaProgressBar()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.btnOK, QtCore.SIGNAL("clicked()"), self.actionOK)
    QtCore.QObject.connect(self.ui.btnExit, QtCore.SIGNAL("clicked()"), self.close)
    QtCore.QObject.connect(self.ui.btnSelectFolder, QtCore.SIGNAL("clicked()"), self.selectDir)
    QtCore.QObject.connect(self.ui.btnSelectFile, QtCore.SIGNAL("clicked()"), self.selectFile)

  def selectDir(self):
    #Вызов стандартного окна выбора существующей папки
    directory = QtGui.QFileDialog.getExistingDirectory(self, _fromUtf8('Выберите папку с изображениями после Magle'),unicode(self.ui.lineFolder.text()))
    if not directory.isNull():
        self.ui.lineFolder.setText(directory)

  def selectFile(self):
    #Вызов стандартного окна выбора файла
    filename = QtGui.QFileDialog.getOpenFileName(self, _fromUtf8('Выберите папку с файлом cbz после Magle'),unicode(self.ui.lineFolder.text()),'cbz files (*.cbz);;All files (*.*)')
    if not filename.isNull():
        self.ui.lineFolder.setText(filename)

  def actionOK(self):
      """ По нажатию ОК обрабатываем папку из текстбокса.
        Проверяем существует ли и не файл ли.
        Берем список файлов и вызываем add_progressbar
        с нужной частотой.
      """
      #Папка читается из строки ввода и может быть полным именем *.cbz файла
      imgdir = unicode(self.ui.lineFolder.text())

      targetdir=imgdir+'_MPB' #Теперь только копирование, оригинальная папка неизменна
      howoften = int(self.ui.spinBox.text())  #Every n-th image

      if not os.path.exists(imgdir):
        QtGui.QMessageBox.warning(self, _fromUtf8('Ошибка!'), imgdir + _fromUtf8(' -- нет такой папки!'))
        return


      if os.path.isfile(imgdir): #Указан прямой путь к файлу архива
        if zipfile.is_zipfile(imgdir):
           archive=zipfile.ZipFile(imgdir,'r')
           newarchivename=imgdir[:-4]+unicode('_MPB')+imgdir[-4:]
           newarchive=zipfile.ZipFile(newarchivename,'w')
           filelist=sorted(archive.namelist())
        else:
           QtGui.QMessageBox.warning(self, _fromUtf8('Ошибка!'), os.path.split(imgdir)[1] + _fromUtf8('-- Не могу окрыть!'))
           return
      else: #Указан путь к папке
        filelist=sorted(os.listdir(imgdir))
        archive=False

      #Count *.png and *.cbz files in dir
      total_png=0
      total_cbz=0
      for filename in filelist:
        if filename[-3:].lower()=='png':
          total_png+=1
        if not archive and filename[-3:].lower()=='cbz':
          total_cbz+=1
          archivename=filename #запомним имя cbz архива

      if total_png==0 and total_cbz==0:
        QtGui.QMessageBox.warning(self, _fromUtf8('Ошибка!'), _fromUtf8('Папка не содержит файлов для обработки!'))
        return
      if total_png==0 and total_cbz>1:
        QtGui.QMessageBox.warning(self, _fromUtf8('Ошибка!'), _fromUtf8('Папка содержит больше одного архива!'))
        return

      if not archive and total_png==0 and total_cbz==1:
        #Был указан путь на папку, которая содержит 1 cbz файл
        imgdir=os.path.join(imgdir,archivename)
        if zipfile.is_zipfile(imgdir):
           archive=zipfile.ZipFile(imgdir,'r')
           newarchivename=imgdir[:-4]+unicode('_MPB')+imgdir[-4:]
           newarchive=zipfile.ZipFile(newarchivename,'w')
           filelist=sorted(archive.namelist())

           total_png=0
           for filename in filelist:
             if filename[-3:].lower()=='png':
               total_png+=1

        else:
           QtGui.QMessageBox.warning(self, _fromUtf8('Ошибка!'), archivename + _fromUtf8('-- Не могу окрыть!'))
           return

      #Start adding progress bar
      cur_png=0 #Current *.png file in dir
      for filename in filelist:
        if filename[-3:].lower()=='png':
          cur_png+=1

          if self.ui.progressBar.value()!=100*cur_png/total_png:
            self.ui.progressBar.setProperty("value", 100*cur_png/total_png)
            app.processEvents() #Не дает зависать GUI

          if cur_png//howoften==float(cur_png)/howoften:
    ##        print str(100*cur_png/total_png)+"%" #Show progress %
            if archive:
              image_io = ImageFile.Parser()
              image_io.feed(archive.read(filename))
              image = image_io.close()
            else:
              image=Image.open(os.path.join(imgdir,filename))

            #Now calling funtion to draw progress bar
            if image.size[1]<=800:
              image = add_progressbar(image, cur_png, total_png,(600,800))
            else:
              image = add_progressbar(image, cur_png, total_png,(824, 1200))



            #Сохраняем
            if archive:
              tmp_fullname=os.path.join(os.path.dirname(targetdir),os.path.basename(filename))
              image.save(tmp_fullname)
              newarchive.write(tmp_fullname,filename)
              #Очистим диск
              try:
                os.remove(tmp_fullname)
              except:
	            pass
            else:
              if not os.path.exists(targetdir):
                 os.mkdir(targetdir)
              image.save(os.path.join(targetdir,filename))

          else: #Здесь те файлы, на которых не надо рисовать прогресс бар
            if archive:
               newarchive.writestr(filename,archive.read(filename))
            else:
              if imgdir!=targetdir:
                if not os.path.exists(targetdir):
                   os.mkdir(targetdir)
                shutil.copy(os.path.join(imgdir,filename),os.path.join(targetdir,filename))

      #Конец работы
      if archive:
        archive.close()
        newarchive.close()


def formatImage(image):
    if image.mode == 'RGB':
        return image
    return image.convert('RGB')

def add_progressbar(image, file_number, files_totalnumber,size):
  """ This function processes image already converted for Kindle
      add_progressbar(image, file_number, files_totalnumber)
      returns modified image """

  widthImg, heightImg = image.size

  #========================================================================
  #Сделаем картинку полной по ширине, для одинаковых размеров прогресс бара

  imageOriginal = image #Сохраним оригинал, чтобы взять из него палитру, если надо

  image = formatImage(image) #Работаем с RGB

  white = (255,255,255) #Белый цвет
  black = (0,0,0) #Черный цвет


  widthDev, heightDev = size
  widthImg, heightImg = image.size

  pastePt = (
        max(0, (widthDev - widthImg) / 2),
        max(0, (heightDev - heightImg) / 2)
    )

  imageBg = Image.new('RGB',size,(255,255,255))

  imageBg.paste(image, pastePt)
  image=imageBg
  widthImg, heightImg = image.size

  #========================================================================

  draw = ImageDraw.Draw(image)
  #Black rectangle
  draw.rectangle([(0,heightImg-3), (widthImg,heightImg)], outline=black, fill=black)
  #White rectangle
  draw.rectangle([(widthImg*file_number/files_totalnumber,heightImg-3), (widthImg-1,heightImg)], outline=black, fill=white)

  #Making notches
  for i in range(1,10):
    if i <= (10*file_number/files_totalnumber):
        notch_colour=white #White
    else:
        notch_colour=black  #Black
    draw.line([(widthImg*float(i)/10,heightImg-3), (widthImg*float(i)/10,heightImg)],fill=notch_colour)
    #The 50%
    if i==5:
        draw.rectangle([(widthImg/2-1,heightImg-5), (widthImg/2+1,heightImg)],outline=black,fill=notch_colour)

  if imageOriginal.mode == 'P':
    image = image.quantize(palette=imageOriginal)

  return image

def main():

  pass

if __name__ == '__main__':
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())