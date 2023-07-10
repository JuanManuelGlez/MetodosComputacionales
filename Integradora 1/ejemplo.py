DEBUG = False # True enables DEBUG output. False disables.
#DEBUG = True
 
# input file describing our DFA
inputFileName = 'three.txt'
 
# all legal operators: concatenation, union, and kleen star
# (everything else in the regular expression will be considered an input symbol)
operators = [ '.', '+', '*' ]
 
# set to False if you see ^[[1m and ^[[0;0m showing up in the output
enableBoldOutput = True
bold = "33[1m"
reset = "33[0;0m"
 
################################################################################
#                                 FUNCTIONS                                    #
################################################################################
 
# prints debug info when DEBUG flag set to True
def debug( msg ):
 
   if( DEBUG ):
      print "DEBUG: " + msg
 
# returns a string representation of the Transition Table in a technical
# human-moar-leik-engineer readable format
def transitionTable2Str():
 
   return str(transitionTable)
 
# returns a string representation of the Transition Table in a technical
# human-moar-leik-engineer readable format
def curSubNfaList2Str():
 
   return str(curSubNfaList)
 
# returns a string representation of the NFA in a human readable format
def automata2Str():
 
   ####################
   # DEFINE VARIABLES #
   ####################
 
   states = ''
   sigma  = ''
   delta  = ''
 
   ###############
   # NFA or DFA? #
   ###############
 
   # do we have epsilon transitions in this Transition Table?
   print epsilon
   if len(transitionTable[0]) > epsilon:
      # we have epsilon transitions in this Transition Table (or at least we
      # have epsilon transitions to [None] in this Transition Table)
      printingNfa = True
   else:
      printingNfa = False
 
   ###################################
   # BUILD HUMAN-READABLE STATES SET #
   ###################################
 
   states += '{'
 
   # LOOP THOUGH ALL ROWS OF THE TRANSITION TABLE
   counter = 0
   while counter < len(transitionTable):
 
      # is this our first state?
      if not states == '{':
         # this is not our first state, so prepend a comma & space
         states += ', '
 
      # the name of each state is merely its index in the Transition Table, so
      # just append the counter to our set of states
      states += str(counter)
 
      counter += 1
 
   states += '}'
 
   #####################################
   # BUILD HUMAN-READABLE ALPHABET SET #
   #####################################
 
   sigma += '{'
   # LOOP THOUGH ALL THE ELEMENTS (SYMBOLS) IN THE ALPHABET
   for symbol in alphabet:
 
      # is this our first symbol?
      if not sigma == '{':
         # this is not our first symbol, so prepend a comma & space
         sigma += ', '
 
      sigma += symbol
 
   sigma += '}'
 
   #########################################
   # BUILD HUMAN-READABLE TRANSITION TABLE #
   #########################################
 
   delta = '           '
 
   # PRINT TOP ROW OF TABLE (SYMBOLS IN ALPHABET)
 
   if enableBoldOutput:
      delta += bold
 
   # loop through all symbols in the alphabet
   for symbol in alphabet:
 
      delta += '{0:^10}'.format( str(symbol) ) + ' '
 
   # are we printing an NFA?
   if printingNfa == True:
      # we are priting an NFA; create a column for epsilon transitions
      delta += '{0:^10}'.format( 'epsilon' ) + ' '
 
   if enableBoldOutput:
      delta += reset
 
   delta += "n"
 
   # ITERATE THROUGH EACH FOLLOWING ROW (STATES)
   counter = 0
   for row in transitionTable:
 
      # print the first element of the row (the transition-from state)
      if enableBoldOutput:
         delta += bold
      delta += '{0: | left "out" State |
#  -----------------         ------------------
#  ------------------         -------------------
# | right "in" State | ----> | right "out" State |
#  ------------------         -------------------
#
# into this:
#  -----         ------        ------        ------
# | LiS | ----> | LoS | ----> | RiS | ----> | RoS |
#  ------        ------        ------        ------
#
def concatenateCurSubNfa():
 
   ###############################
   # ADD ARC TO TRANSITION TABLE #
   ###############################
 
   # we concatenate 2 sub-NFAs by creating an arc from the "left" sub-NFA's
   # "out" State to the "right" sub-NFA's "in" State
 
   # -2 index = "left" sub-NFA
   # 1 subindex = "out" State
   leftExitState = curSubNfaList[-2][1]
 
   # -1 index = "right" sub-NFA
   # 0 subindex = "in" State
   rightEnterState = curSubNfaList[-1][0]
 
   debug( "Adding an epsilon transition from state " +str(leftExitState)+
          " to state " +str(rightEnterState) )
 
   transitionTable[ leftExitState ][ epsilon ] = [rightEnterState]
 
   debug( "tTransition Table = " )
   debug( "tt" + transitionTable2Str() )
 
   #####################################################
   # MERGE SUB-NFAs TO SINGLE SUB-NFA IN curSubNfaList #
   #####################################################
 
   debug( "Merging the 2 sub-NFAs in curSubNfaList" )
 
   # -1 index = "right" sub-NFA
   # 1 subindex = "out" State
   outState = curSubNfaList[-1][1]
 
   # set the "left" sub-NFA's "out" State to be the "right" sub-NFA's "out"
   # State
 
   # -2 index = "left" sub-NFA
   # 1 subindex = "out" State
   curSubNfaList[-2][1] = outState
 
   # ..and delete the now-orphaned "right" sub-NFA
   curSubNfaList.pop()
 
   debug( "tcurSubNfaList = " )
   debug( "tt" + curSubNfaList2Str() )
 
# turn this:
#  ----------------         -----------------
# | top "in" State | ----> | top "out" State |
#  ----------------         -----------------
#  -------------------         --------------------
# | bottom "in" State | ----> | bottom "out" State |
#  -------------------         --------------------
#  ------------------
# | new "left" State |
#  ------------------
#  -------------------
# | new "right" State |
#  -------------------
#
# into this:
#          e   -----         ------
#         --->| TiS | ----> | ToS |
#  ----- /     ------        ------   e    -----
# | NlS |                             ===> | NrS |
#  -----  e   -----         ------ /  e    -----
#         --->| BiS | ----> | BoS |
#              ------        ------
#
def unionCurSubNfa():
 
   #################################
   # ADD 2 STATES TO OUR FINAL NFA #
   #################################
 
   debug( "tTransition Table = " )
   debug( "tt" + transitionTable2Str() )
   # get the current number of States from the number of rows of the transition
   # table. Subtract 1 to start from 0.
   numStates = len( transitionTable ) - 1
 
   newLeftState = numStates+1
   newRightState = numStates+2
 
   debug( 'Adding states ' +str(numStates+1)+' & ' +str(numStates+2)+
          ' to the NFA' )
 
   ##############################################
   # INSERT NEW LEFT STATE INTO TRANSTION TABLE #
   ##############################################
 
   # build a row to add to the Transition Table for our "left" State that has
   # an epsilon transition to each current sub-NFA's "in" State
   row = [ [None] for i in range( len(alphabet) ) ]
 
   # -2 index = "top" sub-NFA
   # 0 subindex = "in" State
   topInState = curSubNfaList[-2][0]
 
   # -1 index = "bottom" sub-NFA
   # 0 subindex = "in" State
   bottomInState = curSubNfaList[-1][0]
 
   debug( "Adding an epsilon transition from state " +str(newLeftState)+ " to "
          "states " +str(topInState)+ " & " +str(bottomInState) )
 
   # add a epsilon transitions to both current sub-NFAs
   row.append( [topInState, bottomInState] )
   transitionTable.append( row )
 
   ###############################################
   # INSERT NEW RIGHT STATE INTO TRANSTION TABLE #
   ###############################################
 
   # build a row to add to the Transition Table for our "right" State with no
   # "out" transitions
   row = [ [None] for i in range( len(alphabet) ) ]
 
   # add a final epsilon transition
   row.append( [None] )
   transitionTable.append( row )
 
   #######################################################
   # INSERT ARC TO NEW RIGHT STATE INTO TRANSITION TABLE #
   #######################################################
 
   # -2 index = "top" sub-NFA
   # 1 subindex = "out" State
   topOutState = curSubNfaList[-2][1]
 
   # -1 index = "top" sub-NFA
   # 1 subindex = "out" State
   bottomOutState = curSubNfaList[-1][1]
 
   debug( "Adding epsilon transitions from states " +str(topOutState)+ " & "
          +str(bottomOutState)+ " to state " +str(newRightState) )
 
   # add an epsilon transition from the top sub-NFA's "out" State to the new
   # "right" State
   transitionTable[ topOutState ][ epsilon ] = [newRightState]
 
   # add an epsilon transition from the top sub-NFA's "out" State to the new
   # "right" State
   transitionTable[ bottomOutState ][ epsilon ] = [newRightState]
 
   debug( "tTransition Table = " )
   debug( "tt" + transitionTable2Str() )
 
   #####################################################
   # MERGE SUB-NFAs TO SINGLE SUB-NFA IN curSubNfaList #
   #####################################################
 
   # "in" State of merged sub-NFA
   curSubNfaList[-2][0] = newLeftState
 
   # "out" State of merged sub-NFA
   curSubNfaList[-2][1] = newRightState
 
   # ..and delete the now-orphaned "bottom" sub-NFA
   curSubNfaList.pop()
 
   debug( "tcurSubNfaList = " )
   debug( "tt" + curSubNfaList2Str() )
 
# turn this:
#  ----------------------         -----------------------
# | current "left" State | ----> | current "right" State |
#  ----------------------         -----------------------
#  ------------------
# | new "left" State |
#  ------------------
#  -------------------
# | new "right" State |
#  -------------------
#
# into this:
#  -----    e    ----- ----> -----    e    -----
# | NlS | ----> | ClS |  e  | CrS | ----> | NrS |
#  -----   e    -----  0):
 
   # get the next token from the beginning of the regularExpression string
   token = regularExpressionList.pop(0)
 
   debug( "WORKING WITH TOKEN '" +str(token)+ "' FROM THE REGULAR EXPRESSION" )
 
   if token in operators:
      # the token is an operation
      subNfaOperation( token )
 
   else:
      # the token is a symbol
      createNfaFromSymbol( token )
 
#####################
# PRINT EPSILON-NFA #
#####################
 
print "The following epsilon-NFA is equivalent to the supplied Regular "
      "Expression (" +str(regularExpression)+ "):"
print automata2Str()
 
#####################################
# CONVERT THE EPSIOLON-NFA TO A DFA #
#####################################
 
debug( "---BEGIN CONVERTING EPSILON-NFA TO A DFA---" )
 
# DEFINE VARIABLES
newTransitionTable = []
newStates = []
addedStates = []
 
# following the Subset Construction Algorithm, the first State of our DFA is the
# Epsilon Closure of the first state of our epsilon-NFA
startState = epsilonClosure( curSubNfaList[0][0] )
newStates.append( startState )
 
while len(newStates) > 0:
 
   newTransitionTable.append( [] )
   state = newStates.pop(0)
   addedStates.append( state )
 
   debug( "Adding State " +str(state)+ " to DFA with new State name = "
          + str(len(newTransitionTable)-1) )
 
   # loop through all symbols in the alphabet + epsilon transitions
   counter = 0
   while counter = len(alphabet):
         symbol = ''
      else:
         symbol = alphabet[counter]
 
      # has this state already been added to the new DFA?
      if not transitionTo == [] and not transitionTo == [None] and not transitionTo in newStates and not transitionTo in addedStates:
         # this state has not already been added to the new DFA; add it to the
         # newStates list so it'll be added in a future iteration
         newStates.append( transitionTo )
 
      if transitionTo in addedStates:
         newStateIndex = addedStates.index( transitionTo )
      elif transitionTo in newStates:
         newStateIndex = newStates.index(transitionTo) + len(newTransitionTable)
 
      debug( "Adding transition from State " +str(state)+ " = "
             +str(len(newTransitionTable)-1)+ " to State " +str(transitionTo)
             +" = " +str(newStateIndex)+ " on input symbol '" +str(symbol)+ "'"
             )
 
      newTransitionTable[ len(newTransitionTable)-1 ].append( extendedDelta( state, counter ) )
      counter += 1
 
   debug( "tTransition Table = " )
   debug( "tt" + transitionTable2Str() )
 
# overwrite the transitionTable with the new one now that we no longer need it
# (automata2Str() uses transitionTable)
transitionTable = newTransitionTable
 
#############
# PRINT DFA #
#############
 
print ("The following DFA is equivalent to the above epsilon-NFA and the "
      "original Regular Expression (" +str(regularExpression)+ "):")
print automata2Str()
 
################
# EXIT CLEANLY #
################
 
exit(0)