import board
print(dir(board))

from kmk.kmk_keyboard import KMKKeyboard

from kb import varList

from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split
from kmk.modules.layers import Layers
from kmk.modules.oneshot import OneShot
from kmk.modules.combos import Combos, Chord, Sequence

keyboard = KMKKeyboard()

keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.debug_enabled = True

split = Split(
    data_pin=board.RX,
    #data_pin=varList.data_pin,
    data_pin2=board.TX,
    uart_flip=True,
    #data_pin2=varList.data_pin2,
    #split_side=varList.ss,
    split_flip=True,
    #use_pio=True,
)

keyboard.modules.append(split)

layers_ext = Layers()
keyboard.modules.append(layers_ext)

oneshot = OneShot()
keyboard.modules.append(oneshot)

combos = Combos()
keyboard.modules.append(combos)

keyboard.col_pins = varList.col_pins
keyboard.row_pins = varList.row_pins

_____ = KC.TRNS
XXXXX = KC.NO

SYMBS = KC.OS(KC.MO(1))
NUMBS = KC.OS(KC.MO(2))
#VIMESC = KC.OS(KC.MO(3))
THIRD = KC.MO(3)
KEYPD = KC.MO(4)
#BKVIM = KC.LT(4, KC.BSPC)
#DELVIM = KC.LT(5, KC.DEL)

# garbage key map just for testing
keyboard.keymap = [
    #[   #letters
    #    XXXXX,	    KC.ESC,     KC.L,	    KC.U,	  KC.J,           KC.K,	    KC.M,	  KC.W,    KC.EXLM,  XXXXX,
    #    KC.BSPC,     KC.A,      KC.N,	    KC.I,	  KC.S,	        KC.H,	    KC.T,	  KC.R,	   KC.O,  KC.Q,
    #    KC.BSPC,    KC.A,	    KC.X,	    KC.Y,	  KC.F,	        KC.P,	    KC.G,	  KC.Z,	   KC.O,     KC.Q,
    #    KC.C,       KC.V,	    LOWER,  KC.SPC,	  KC.BSPC,	    KC.DEL,	    KC.E,     RAISE, KC.B,    KC.D,
    #],
    [   #letters top row swapped
        XXXXX,		KC.RWIN,	KC.X,	    KC.Y,	  KC.J,         KC.K,	    KC.G,	  KC.Z,		KEYPD,	XXXXX,
        KC.LCTL,	KC.LALT,	KC.N,	    KC.I,	  KC.S,	        KC.H,	    KC.T,	  KC.R,		KC.HOME,		KC.END,
        KC.ESC,		KC.A,	    KC.L,	    KC.U,	  KC.F,	        KC.P,	    KC.M,	  KC.W,		KC.O,		KC.Q,
        #KC.V,		KC.C,	    BKVIM,      KC.SPC,	  LOWER,	    RAISE,	    KC.E,	  DELVIM,	KC.D,		KC.B,
        KC.V,		KC.C,	    SYMBS,      KC.E,	  KC.BSPC,	    KC.LSFT,	KC.SPC,	  NUMBS,	KC.D,		KC.B,
    ],
    [   #Symbols
        XXXXX,   KC.LABK,   KC.GRV,		KC.BSLS,	KC.PERC,		KC.DLR,	    KC.SLSH,  KC.TILD,  KC.RABK,    XXXXX,
        KC.BSPC, KC.LBRC,   KC.LCBR,	KC.LPRN,	KC.COLN,		KC.SCLN,    KC.RPRN,  KC.RCBR,  KC.RBRC,    KC.CIRC,
        KC.BSPC, KC.LBRC,   KC.EXLM,	KC.EXLM,	KC.AT,			KC.HASH,    KC.EXLM,  KC.EXLM,  KC.RBRC,    KC.CIRC,
        KC.EXLM, KC.PIPE,   XXXXX,		KC.EXLM,		_____,			_____,	    KC.SPC,     THIRD,  KC.AMPR,    KC.QUES,
    ],
    #[  #Numbers
    #    XXXXX,      KC.ESC,     KC.QUOT,    KC.UNDS,  KC.ASTR,      KC.N7,	    KC.N8,	  KC.N9,    KC.EXLM,    XXXXX,
    #    KC.EXLM,    KC.EXLM,    KC.DQT,	    KC.EQL,	  KC.COMM,      KC.N4,	    KC.N5,	  KC.N6,	KC.EXLM,    KC.EXLM,
    #    KC.BSPC,    KC.DOT,     KC.EXLM,    KC.EXLM,  KC.SLSH,      KC.N1,	    KC.N2,	  KC.N3,	KC.N0,      KC.EXLM,
    #    KC.PLUS,    KC.MINS,    KC.N1,      KC.SPC,	  KC.ENT,       RAISE,	    KC.EXLM,  KC.ENT,   KC.SLSH,    KC.ASTR,
    #],
    [   #numbers unorthodox
        XXXXX,      KC.ESC,     KC.QUOT,    KC.UNDS,  KC.ASTR,      KC.N7,	    KC.N8,	  KC.N9,    KC.EXLM,    XXXXX,
        KC.BSPC,    KC.DOT,     KC.DQT,	    KC.EQL,	  KC.COMM,      KC.N0,	    KC.N1,	  KC.N2,	KC.N5,    KC.EXLM,
        KC.BSPC,    KC.DOT,     KC.EXLM,    KC.EXLM,  KC.SLSH,      KC.N6,	    KC.N4,	  KC.N3,	KC.N5,      KC.EXLM,
        KC.PLUS,    KC.MINS,    THIRD,      KC.TAB,	  KEYPD,       KEYPD,	    KC.EXLM,  XXXXX,   KC.SLSH,    KC.ASTR,
    ],
    [   #numbers unorthodox
        XXXXX,      _____,      _____,      _____,     _____,      _____,	    _____,	  _____,    KC.TO(0),    XXXXX,
        _____,      _____,      _____,      _____,     KC.QUES,      KC.EXLM,	_____,	  _____,    _____,    _____,
        _____,      _____,      _____,      _____,     _____,      _____,	    _____,	  _____,    _____,    _____,
        _____,      _____,      KC.ESC,     _____,     _____,      _____,	    _____,	  KC.ESC,   _____,    _____,
    ],
    [   #number pad / blender?
        XXXXX,      KC.ESC,     KC.QUOT,    KC.UNDS,  KC.PAST,      KC.P7,	    KC.P8,	  KC.P9,    KC.EXLM,    XXXXX,
        KC.BSPC,    KC.PDOT,    KC.DQT,	    KC.PEQL,  KC.PCMM,      KC.P3,	    KC.P5,	  KC.P5,	KC.N0,      KC.PENT,
        KC.BSPC,    KC.PDOT,    KC.EXLM,    KC.EXLM,  KC.PSLS,      KC.P1,	    KC.P2,	  KC.P3,	KC.N0,      KC.PENT,
        KC.PPLS,    KC.PMNS,    XXXXX,      KC.SPC,	  XXXXX,       XXXXX,	    KC.EXLM,  XXXXX,   KC.PSLS,    KC.PAST,
    ],
    #[   #numbers unorthodox
    #    XXXXX,      _____,      _____,      _____,     _____,      _____,	    _____,	  _____,    _____,    XXXXX,
    #    _____,      _____,      _____,      _____,     _____,      _____,	    _____,	  _____,    _____,    _____,
    #    _____,      _____,      _____,      _____,     _____,      _____,	    _____,	  _____,    _____,    _____,
    #    _____,      _____,      KC.NO,     _____,     _____,      _____,	    _____,	  KC.ESC,   _____,    _____,
    #],
    #[   #numbers unorthodox
    #    XXXXX,      _____,      _____,      _____,     _____,      _____,	    _____,	  _____,    _____,    XXXXX,
    #    _____,      _____,      _____,      _____,     _____,      _____,	    _____,	  _____,    _____,    _____,
    #    _____,      _____,      _____,      _____,     _____,      _____,	    _____,	  _____,    _____,    _____,
    #    _____,      _____,      KC.ESC,     _____,     _____,      _____,	    _____,	  KC.NO,    _____,    _____,
    #],
]

combos.combos = [
    Chord((KC.LSHIFT, KC.BSPACE), KC.ENTER),
    Chord((KC.LSHIFT, KC.ESC), KC.DEL),
]

if __name__ == "__main__":
    keyboard.go()
