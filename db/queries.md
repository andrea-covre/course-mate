# Useful queires for the database

## Majors

### Obtain all majors with corresponding subject code:

```sql
SELECT major.id, major.level, major.name, subject.code
FROM major
LEFT JOIN subject ON major.name = subject.name;
```

Output sample:

| id | level | name | code |
| --- | --- | --- | --- |
| 132 | BS | Aerospace Engineering | AE |
| 173 | MS | Architecture | ARCH |
| 231 | Phd | Biomedical | BMED |
