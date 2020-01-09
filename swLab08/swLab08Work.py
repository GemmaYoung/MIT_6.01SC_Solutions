import lib601.le as le
import lib601.circ as circ

ce = le.EquationSet()
# Enter your equations here
##ce.addEquation(le.Equation([1.0, -1,0], ['e3', 'e0'], 10.0))
##ce.addEquation(le.Equation([  ##It will be too tedious to add all the equations, so I skip them.
##print ce.solve()

ce1 = circ.Circuit([circ.VSrc(10, 'e3', 'e0'), circ.Resistor(100, 'e3', 'e1'),
                    circ.Resistor(10, 'e1', 'e0'), circ.Resistor(100, 'e1', 'e2'),
                    circ.Resistor(100, 'e3', 'e2'), circ.Resistor(100, 'e2', 'e0')])
    # Enter your circuit components here
print ce1.solve('e0')
