import pickle

class No:
    def __init__(self, chave, no_esquerdo, no_direito):
        self.chave = chave
        self.no_esquerdo = no_esquerdo
        self.no_direito = no_direito
    
    def exibir_chave(self):
        print(self.chave)

class BinaryTree:
    

    def __init__(self) -> None:
        self.raiz = None
        self.__total_nos:int = 0
        self.array = []
    
    def inserir_chave(self, chave):
        """
            insere uma nova chave na árvore.
            Parametros obrigatorios: chave a ser inserida
        """
        novo_no = No(chave, None, None)

        if self.raiz == None:
            self.raiz = novo_no
            self.__total_nos += 1
        else:
            no_atual = self.raiz

            while True:
                no_anterior = no_atual

                if chave <= no_atual.chave:
                    no_atual = no_atual.no_esquerdo

                    if no_atual == None:
                        no_anterior.no_esquerdo = novo_no
                        self.__total_nos += 1
                        return
                else:
                    no_atual = no_atual.no_direito
                    if no_atual == None:
                        no_anterior.no_direito = novo_no
                        self.__total_nos += 1
                        return
    
    def get_total_nos(self) -> int:
        """
            retorna a quantidade de nós da árvore
        """
        return self.__total_nos

    def pre_ordem(self, raiz:No):
        """
            imprime os elementos da árvore em pre ordem.
            Parametros obrigatorios: 'instancia.raiz'
        """
        if raiz is not None:
            raiz.exibir_chave()
            self.em_ordem(raiz.no_esquerdo)
            self.em_ordem(raiz.no_direito)
    
    def em_ordem(self, raiz:No):
        """
            imprime os elementos da árvore em ordem.
            Parametros obrigatorios: 'instancia.raiz'
        """
        if raiz is not None:
            self.pre_ordem(raiz.no_esquerdo)
            raiz.exibir_chave()
            self.pre_ordem(raiz.no_direito)
    
    def pos_ordem(self, raiz:No):
        """
            imprime os elementos da árvore em pós ordem.
            Parametros obrigatorios: 'instancia.raiz'
        """
        if raiz is not None:
            self.pos_ordem(raiz.no_esquerdo)
            self.pos_ordem(raiz.no_direito)
            raiz.exibir_chave()
    
    def altura(self, raiz:No) -> int:
        """
            retorna a altura maxima da árvore.
            Parametros obrigatorios: 'instancia.raiz'
        """
        if raiz is None:
            return - 1
        else:
            altura_esquerda = self.altura(raiz.no_esquerdo)
            altura_direita = self.altura(raiz.no_direito)

        if altura_esquerda < altura_direita:
            return altura_direita + 1
        else:
            return altura_esquerda + 1
    
    def buscar_elemento(self, chave) -> No:
        """
            retorna um no da arvore caso o elemento a ser procurado exista. caso contrario retorna None.
            Parametros obrigatorios: chave a ser procurada
        """

        if self.raiz == None:
            return None
        else:
            no_atual = self.raiz
            while chave != no_atual.chave:
                if chave < no_atual.chave:
                    no_atual = no_atual.no_esquerdo
                else: 
                    no_atual = no_atual.no_direito
                if self.eh_folha(no_atual):
                    return None

            return no_atual
    
    def eh_folha(self, no: No) -> bool:
        """
            verifica se um elemento da arvore é folha.
            retorna True caso seja e False caso contrario.
            parametros obrigatorios: um nó da arvore
        """
        if no is not None:
            if no.no_esquerdo == None and no.no_direito == None:
                return True
        return False
    
    def no_sucessor(self, apagar:No):
        pai_no_sucessor:No = apagar
        no_sucessor:No = apagar   
        no_atual:No = apagar.no_direito

        while no_atual != None:
            pai_no_sucessor = no_sucessor
            no_sucessor = no_atual
            no_atual = no_atual.no_esquerdo
        
        if no_sucessor != apagar.no_direito:
            pai_no_sucessor.no_esquerdo = no_sucessor.no_direito
            no_sucessor.no_direito = apagar.no_direito
        
        return no_sucessor
    
    def remover_chave(self, chave):
        """
        apaga um nó da arvore.
        paramentros obrigatorios: a chave que deseja remover
        retorna True caso a chave seja encontrada. Caso contrario, retorna False 
        """

        if self.raiz == None:
            return False

        no_atual = self.raiz
        no_pai = self.raiz
        existe_filho_esquerdo = True

        while no_atual.chave != chave:
            no_pai = no_atual
            if chave < no_atual.chave:
                no_atual = no_atual.no_esquerdo
                existe_filho_esquerdo = True
            else:
                no_atual = no_atual.no_direito
                existe_filho_esquerdo = False
            
            if no_atual == None:
                return False
        
        if no_atual.no_esquerdo == None and no_atual.no_direito == None:
            if no_atual == self.raiz:
                self.raiz = None
            else:
                if existe_filho_esquerdo:
                    no_pai.no_esquerdo = None
                    
                else:
                    no_pai.no_direito = None
                    
        elif no_atual.no_direito == None:
            if no_atual == self.raiz:
                self.raiz = no_atual.no_esquerdo
            else:
                if existe_filho_esquerdo:
                    no_pai.no_esquerdo = no_atual.no_esquerdo
                else:
                    no_pai.no_direito = no_atual.no_esquerdo
        
        elif no_atual.no_esquerdo == None:
            if no_atual == self.raiz:
                self.raiz = no_atual.no_direito
            else:
                if existe_filho_esquerdo:
                    no_pai.no_esquerdo = no_atual.no_direito
                else:
                    no_pai.no_direito = no_atual.no_direito

        else:
            no_sucessor = self.no_sucessor(no_atual)

            if no_atual == self.raiz:
                self.raiz = no_sucessor
            else:
                if existe_filho_esquerdo:
                    no_pai.no_esquerdo = no_sucessor
                else:
                    no_pai.no_direito = no_sucessor
            
            no_sucessor.no_esquerdo = no_atual.no_esquerdo

        return True
    
    def ler_arvore_do_arquivo(self, raiz:No, path:str, nome_arquivo:str):
        """
            Parametros obrigatorios: 'instancia.raiz',
            path: caminho de onde deseja ler o arquivo;
            nome_arquivo: nome do arquivo a ser lido;
        """
        print("carregando arquivo...")
        try:
            arquivo = open(path+"/"+nome_arquivo, 'rb')
            self.array = pickle.load(arquivo)
            arquivo.close()

            if len(self.array) > 0 :
                for chave in self.array:
                    self.inserir_chave(chave) 

            self.array.clear()
            print("carregado com sucesso...")

            return True
        except:
            print("erro ao ler arquivo. verifique o path e nome do arquivo")
        
        return False
       
    def _prencher_array(self, raiz:No):
        if raiz is not None:
            self.array.append(raiz.chave)
            self._prencher_array(raiz.no_esquerdo)
            self._prencher_array(raiz.no_direito)
        
        if len(self.array) > 0:
            return True
        
        return False
    

    def salvar_arvore_no_arquivo(self, raiz:No, path:str, nome_arquivo:str):
        """
            Parametros obrigatorios: 'instancia.raiz'.
            path: caminho onde deseja salvar o arquivo;
            nome_arquivo: nome que desenja dar ao arquivo;
        """
        if self._prencher_array(raiz):
            try:
                arquivo = open(path+"/"+nome_arquivo, 'wb')
                pickle.dump(self.array, arquivo)
                arquivo.close()
                self.array.clear()
                print("arvore salva com sucesso..")
                return True
            except:
                print("erro ao ler arquivo. verifique o path e nome do arquivo")
        
        return False



"""
import os
arvore = BinaryTree()

arvore.ler_arvore_do_arquivo(arvore.raiz, "C:/Users/joaoc/Documents/UFPI/POO2/Criação de pacotes em python/pysimpletree/arquivo_arvore", "arquivo_arvore")
arvore.pre_ordem(arvore.raiz)
path = os.getcwd()
arvore.salvar_arvore_no_arquivo(arvore.raiz, os.getcwd(), "arquivo_arvore")

arvore.inserir_chave(5)
arvore.inserir_chave(6)
arvore.inserir_chave(7)
arvore.inserir_chave(4)
arvore.inserir_chave(3)
arvore.inserir_chave(8)

arvore.remover_chave(6)
arvore.remover_chave(4)
arvore.remover_chave(5)


arvore.em_ordem(arvore.raiz)
"""

"""




print("\ntotal de nós da arvore: " + str(arvore.get_total_nos()))
print("\naltura da arvore: " + str(arvore.altura(arvore.raiz)))

dado = arvore.buscar_elemento(7)
if dado != None:
    print("elemento encontrado: " + str(dado.chave))
else:
    print("elemento não encontrado")

arvore.remover_chave(3)
arvore.remover_chave(7)
arvore.em_ordem(arvore.raiz)

print(arvore.array)
"""

