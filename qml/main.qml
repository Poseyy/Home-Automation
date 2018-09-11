import QtQuick 2.7
import QtQuick.Controls 2.3

ApplicationWindow {
    id: window
    title: "Home Automation App"
    visible: true
    height: 600
    width: 800

    property int lightTracker: 0

    Rectangle {
        anchors.fill: parent
        color: "#2B2C31"
    }
    Rectangle {
        id: topRect
        z: 100
        //color: "#2A2C31"
        color: "#3A3E46"
        anchors.top: parent.top
        anchors.left: parent.left
        width: parent.width
        height: 75
    }
    Label{
        id: page1title
        z: 105
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: topRect.verticalCenter
        text: "Welcome to the Home Automation Project"
        font.pixelSize: 18
        font.family: "Brandon Grotesque"
        color: "white"
    }
    Label{
        id: temperatureLabel
        z: 105
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: topRect.bottom
        anchors.topMargin: 130
        text: "Temperature"
        font.pixelSize: 25
        font.family: "Brandon Grotesque"
        color: "white"
    }
    Label{
        id: temp
        z: 105
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: temperatureLabel.bottom
        anchors.topMargin: 10
        text: "71°F"
        font.pixelSize: 22
        font.family: "Brandon Grotesque"
        color: "white"
    }
    Label{
        id: humidityLabel
        z: 105
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: temp.bottom
        anchors.topMargin: 20
        text: "Humidity"
        font.pixelSize: 25
        font.family: "Brandon Grotesque"
        color: "white"
    }
    Label{
        id: hum
        z: 105
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: humidityLabel.bottom
        anchors.topMargin: 10
        text: "40% RH"
        font.pixelSize: 22
        font.family: "Brandon Grotesque"
        color: "white"
    }
    Label{
        id: lightLabel
        z: 105
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: hum.bottom
        anchors.topMargin: 20
        text: "Lighting"
        font.pixelSize: 25
        font.family: "Brandon Grotesque"
        color: "white"
    }
    Label{
        id: light
        z: 105
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: lightLabel.bottom
        anchors.topMargin: 10
        text: lightTracker === 0 ? "Off" : "On"
        font.pixelSize: 22
        font.family: "Brandon Grotesque"
        color: "white"
    }
}
