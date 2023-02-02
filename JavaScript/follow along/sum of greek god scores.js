const mystudents = [
    {
        firstName:'Zues',
        grade    :86
    },
    {
        firstName: 'Artemis',
        grade    : 97
    },
    {
        firstName:'Hera',
        grade    : 72
    },
    {
        firstName:'Apollo',
        grade    : 90
    }
];
Average = 0
for (let i = 0; i < mystudents.length; i++){
    let grades = mystudents[i];
    Average += grades.grade;
};
console.log(Average/mystudents.length)