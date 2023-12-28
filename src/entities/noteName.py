class NoteName:
    PAUSE = 'Pause'
    DO = 'C'
    RE = 'D'
    MI = 'E'
    FA = 'F'
    SOL = 'G'
    LA = 'A'
    TI = 'B'
    order = [
        DO,
        RE,
        MI,
        FA,
        SOL,
        LA,
        TI,
    ]
    # C maj
    nameToOrderMap = {
        DO: 0,
        RE: 1,
        MI: 2,
        FA: 3,
        SOL: 4,
        LA: 5,
        TI: 6,
    }
    nameToRussianName = {
        DO: "До",
        RE: "Ре",
        MI: "Ми",
        FA: "Фа",
        SOL: "Соль",
        LA: "Ля",
        TI: "Си",
    }

