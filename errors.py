# if:  line 1 : ' ' => space , 'if' => keyword , ':' => del




#if 5:  
#print("  

#line 1: 'if' => keyword ,' ' => space, '5' => number, ':' => del
#line 2: 'print' => id , '(' => del, ' " ' => Unknown => syntax error

# Since the can not detect the string token ,
# before the indentation error is taken in the parsing stage,
# the token error is first taken in the lexical analysis stage.


# space  is a seperator character
      # example:
      #1) for i in => space char seprate this tokens.
          #for,i,in is 3 Separately tokens
          #Whether by a sopace or ten space. There is no problem => for     i in
      #2)a b = 2  Here, a and b are two separate identifier tokens
      # and there is no error in the lexical analysis stage,
      # but in parsing and in the structure of two  the identifier tokens before = has no meaning.

      #3)



#line 1: 'if' => keyword ,' ' => space, '5' => number, ':' => del
#line 2: 'print' => id , '(' => del, '5' => number

# syntax error => Syntactic structural error for indentation in parsing stage


