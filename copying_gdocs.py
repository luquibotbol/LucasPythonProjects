INDX( 	 �\!�           (   8   �       �h                                 )�    ���B�n����B�n����B�n����B�n�0       )               M A N I F E S T - 0 0 0 0 0 1               )�    ���B�n����B�n����B�n����B�n�0       )               M A N I F E ~ 1                     ���B�n����B�n����B�n�0       )               M A N I F E ~ 1                     ���B�n����B�n����B�n����B�n�0       )               M A N I F E ~ 1                     ���B�n����B�n����B�n����B�n 0       )               M A N I F E ~ 1                     )�    ���B�n����B�n����B�n����B�n�0       )               M A N I F E ~ 1                     1                      driver.find_element_by_name('password')
pas.send_keys(password)
pas.send_keys(Keys.RETURN)
driver.implicitly_wait(15)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'kix-zoomdocumentplugin-outer'))
    )
    print('hola')
    print(main.text)
    wit io.open(document, "w+", encoding="utf-8") as f:
        f.write(main.text)
        f.read()



finally:
    driver.close()
