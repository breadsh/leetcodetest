
def questionone(result,numx,numy):

    if numx % numy==0:
        result=result+numx/numy
        return result
    elif numx % numy==numx:
        val=numx*10/numy
        return result+'('+str(val)+')'
        #result='0.'
    else:
        if numx/numy==0:
            result='0.'
        else:
            result=result+str(numx/numy)
            if len(result)==1:
                result=result+'.'
        print result
        numx=(numx%numy)*10
        print numx
        questionone(result,numx,numy)

if __name__=='__main__':
    result=''
    numx=8
    numy=3
    print questionone(result,numx,numy)



