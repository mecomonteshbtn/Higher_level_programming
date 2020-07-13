def compruebamail(mailUsuario):
    """
    La función comprueba si se ingresa un usuario con 
    un solo @, de lo contrario es incorrecto.
    
    >>>compruebamail('mecomontes@gmail.com')
    True
    
    >>>compruebamail('meco.mail@')
    False

    >>>compruebaemail('asad@aslkf@.c')
    False

    >>>compruebaemail('asfklns')
    False

    """
    arroba = mailusuario.count('@')
    if arroba != 1 or mailusuario.rfind('@') == (len(mailusuario) - 1) or mailusuario.find('@') == 0:
        return False
    else:
        return True

