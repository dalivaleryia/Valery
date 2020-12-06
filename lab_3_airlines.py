class Airline:
    def __init__(self, destination, flightNumber, aircraftType, departureTime, daysWeek):
        self.__destination = destination
        self.__flightNumber = flightNumber
        self.__aircraftType = aircraftType
        self.__departureTime = departureTime
        self.__daysWeek = daysWeek

    def getDestination(self):
        return self.__destination

    def getFlightNumber(self):
        return self.__flightNumber

    def getAircraftType(self):
        return self.__aircraftType

    def getDepartureTime(self):
        return self.__departureTime

    def getDaysWeek(self):
        return self.__daysWeek

    def showFlightInfo(self):
        print("\nDestination:\t", self.getDestination(), "\nFlight number\t",
              self.getFlightNumber(), "\nAicreft type:\t", self.__aircraftType, "\nDeparture time:\t", self.__departureTime, "\nDays of week:\t",
              self.__daysWeek, "\n-----------------------\n")


class Airlines:
    __list_airplanes = []

    def addAirplane(self, NewAirline):
        self.__list_airplanes.append(NewAirline)

    def searchByDestination(self, destination):
        __flag = True
        print("By destination:")
        resultTable = list(filter(lambda x: x.getDestination() == destination, self.__list_airplanes))
        for i in resultTable:
            i.showFlightInfo()
            __flag = False
        if(__flag == True):
            print("No records found.")

    def searchByDaysOfWeek(self, daysWeek):
        __flag = True
        print("By day:")
        resultTable = list(filter(lambda x: x.getDaysWeek().find(daysWeek) != -1, self.__list_airplanes))
        for i in resultTable:
            i.showFlightInfo()
            __flag = False
        if(__flag == True):
            print("No records found.")

Airline = [
    Airline("Rome", "A1880", "1", "09:05", "1/3/5/7"),
    Airline("Paris", "A1001", "2", "18:45", "2/4/7"),
    Airline("Rome", "A1880", "2", "21:40", "2/7"),
    Airline("Paris", "A0020", "1", "13:40", "3/6")
          ]

allTable = Airlines()

for i in range(len(Airline)):
    allTable.addAirplane(Airline[i])

allTable.searchByDestination("Rome")

allTable.searchByDaysOfWeek("3")
