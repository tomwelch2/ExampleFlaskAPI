const fs = require("fs");
const mysql = require("mysql2");
const sleep = require("system-sleep");
require("dotenv").config({path: __dirname + '/.env'});

//Script takes JSON file regarding COVID-19 and loads it into MySQL Database ---

sleep(10000);

var data = fs.readFileSync("/app/covid-19.json", "utf8");

data = JSON.parse(data);

const mysqlcon = mysql.createConnection({
    host: process.env.MYSQL_HOST,
    port: 3306,
    user: process.env.MYSQL_USER,
    password: process.env.MYSQL_PASSWORD,
    database: "mydb"
});

mysqlcon.query("CREATE TABLE IF NOT EXISTS mydb.users (`username` VARCHAR(50), `password` VARCHAR(50))", (err, res) => {
    if (err) {throw err};
});

mysqlcon.query("INSERT INTO mydb.users VALUES('admin', 'admin')", (err, res) => {
    if (err) {throw err};
});

mysqlcon.query(
    "CREATE TABLE IF NOT EXISTS mydb.covid \
    (region VARCHAR(50), territory VARCHAR(50), `name` VARCHAR(60), \
    daysSinceLastCase INT, transmissionType INT, newDeaths INT, deaths INT, \
    cases INT, newCases INT, reportDate VARCHAR(50), reportNumber INT)"
)

data.forEach(item => {
    mysqlcon.query(
        `INSERT INTO mydb.covid VALUES \
        ('${item.region}', '${item.territory}', '${item.region}', \
        ${item.daysSinceLastCase}, ${item.transmissionType}, ${item.newDeaths}, \
        ${item.deaths}, ${item.cases}, ${item.newCases}, \
        '${item.reportDate}', ${item.reportNumber})`
    );
});