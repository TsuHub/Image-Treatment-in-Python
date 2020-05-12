# Image-Treatment-in-Python

Temos quatro códigos:
1) ConversorVideoRGBtoGREY.py
2) Grey.py
3) GreyAndSmoothing.py
4) OtsuBinarization.py

Destes códigos, apenas o primeiro faz tratamento com vídos, o restante dos códigos
tratam imagens de formato jpg.

1) Converte um vídeo de formato mp4 colorido para um vídeo em escala cinza (para o mesmo formato).

2) Faz o tratamento da imagem, convertendo-a para a uma escala cinza.

3) Faz o tratamento da imagem, deixando-a cinza e suavizada.

4) Esse é o processo da Binarização de Otsu (Otsu's Binarization).
   Dado um histograma da quantidade de pixels da imagem pela escala de cinza (de 0 a 255),
   o algoritmo trata de converter qualquer cor de escala menor que 127 para branco, e maior,
   para preto, tornando a imagem de cor binária, i.e., preto ou branco.
   
===================================================================================================

MODO DE USO:

Na quarta linha (dos quatro códigos)

	img = cv2.imread("images/Placa 2.jpg")

colocar o caminho onde está contida a imagem em formato jpg, ou
o vídeo em formato mp4, para o tratamento da imagem desejada.