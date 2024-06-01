import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model
        self._currentCountry=None

    def handleCalcola(self, e):
        self.view._txt_result.controls.clear()
        try:
            value=int(self.view._txtAnno.value)
            if value in range(1816,2017):
                self.view._txt_result.controls.append(ft.Text(f"OK"))
                self.model.creaGrafo(value)
                self.view._txt_result.controls.append(ft.Text(f"Grafo creato con {self.model.getNConn()} connected comps"))
                nodes=self.model.getNodes()
                for node in nodes:
                    self.view._txt_result.controls.append(ft.Text(f"{node} - {self.model.degNode(node)}"))
                self._fillDD()
                self.view.btnRagg.disabled = False






            else:
                self.view._txt_result.controls.append(ft.Text(f"Intero deve essere tra 1816 e 2016"))


        except ValueError:
            self.view._txt_result.controls.append(ft.Text(f"Non è stato possibile convertire in intero l'input!"))

        self.view.update_page()

    def getStatiRagg(self,e):
        self.view._txt_result.controls.clear()

        co=self._currentCountry
        if co is None:

            self.view._txt_result.controls.append(ft.Text(f"Non hai ancora scelto uno stato!"))
        else:
             #metodo 1
            #lista=self.model.getCompConn(co)

            #metodo2
            #lista=self.model.daiNodi(co)

            #metodo3
            lista=self.model.algorIter(co)



            for el in lista:

                self.view._txt_result.controls.append(ft.Text(f"{el}"))

        self.view.update_page()

    def _fillDD(self):
        allStati = self.model.getNodes()

        for s in allStati:
            self.view.dd.options.append(ft.dropdown.Option(text=s.StateNme,
                                                                  data=s,
                                                                  on_click=self.read_DD_Stato))

    def read_DD_Stato(self, e):
        print("read_DD_Stato called ")
        if e.control.data is None:
            self._currentCountry = None
        else:
            self._currentCountry = e.control.data

        print(self._currentCountry)