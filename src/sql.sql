
CREATE TABLE IF NOT EXISTS equipas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    logo TEXT NOT NULL,
    titulos INTEGER DEFAULT 0,
    orcamento REAL DEFAULT 0.0
);

INSERT INTO equipas (nome, logo, titulos, orcamento) VALUES
('Ajax', 'ajax.png', 36, 200.0),
('AS Roma', 'as_roma.png', 3, 150.0),
('Atlético de Madrid', 'atletico_madrid.png', 11, 350.0),
('Barcelona', 'barcelona.png', 97, 750.0),
('Bayern de Munique', 'bayern_de_munique.png', 80, 700.0),
('Borussia Dortmund', 'borrussia_dortmund.png', 19, 300.0),
('Chelsea', 'chelsea.png', 34, 600.0),
('Inter de Milão', 'inter_milan.png', 31, 400.0),
('Juventus', 'juventus.png', 69, 450.0),
('Leipzig', 'leipzig.png', 3, 180.0),
('Liverpool', 'liverpool.png', 67, 550.0),
('Manchester City', 'manchester_city.png', 28, 620.0),
('Manchester United', 'manchester_united.png', 68, 650.0),
('Paris Saint-Germain', 'psg.png', 50, 500.0),
('Real Madrid', 'real_madrid.png', 99, 800.0);
