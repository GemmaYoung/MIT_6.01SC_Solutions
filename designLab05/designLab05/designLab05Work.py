import lib601.sig as sig
import lib601.ts as ts
import lib601.poly as poly
import lib601.sf as sf

def controller(k):
   return sf.Gain(k)

def plant1(T):
   return sf.Cascade(sf.Gain(T), sf.FeedbackAdd(sf.R(), sf.Gain(1)))

def plant2(T, V):
   return sf.Cascade(sf.Gain(V*T), sf.FeedbackAdd(sf.R(), sf.Gain(1)))

def wallFollowerModel(k, T, V):
   return sf.FeedbackSubtract(sf.Cascade(controller(k), sf.Cascade(plant1(T), plant2(T, V))), sf.Gain(1))

print wallFollowerModel(1, 0.1, 0.1).dominantPole()
