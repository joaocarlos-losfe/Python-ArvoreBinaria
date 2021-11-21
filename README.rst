.. image:: https://img.shields.io/pypi/v/pysimpletree.svg?style=flat-square
        :target: https://pypi.org/project/pysimpletree/

.. image:: https://img.shields.io/pypi/l/Tree.svg?style=flat-square
        :target: https://github.com/joaocarlos-losfe/pysimpletree/blob/main/LICENSE.txt

PYSIMPLESTREE
-------------

Pacote python para criação de árvores binárias de busca
=======================================================

Criadores
=========


        * `João Carlos <https://github.com/joaocarlos-losfe>`_
        
        * `Vitor Santos <https://github.com/viktorsht>`_

.. image:: https://www.ime.usp.br/~pf/algoritmos/aulas/img/binary-search-tree-sorted-array-animation.gif

O pacote pysimpletree é responsável por fornecer as operações básicas de uma árvores binária de busca para o programador. Assim, o programador,será poupado de realizar a implementação da árvore binária de busca.

O pacote fornece as funções de operações básicas da árvore.
  
   * Inserção
   * Remoção
   * Impressão em pré - Ordem
   * Impressão em pós - Ordem
   * Quantidade de nós
   * Altura da árvore
   * Busca por elementos
   * Salvar em arquivo ou recuperar 

Instalação
==========

.. code-block:: bash

    $ pip install pysimpletree
    
Exemplo de uso do código
========================
.. code-block:: python

  from pysimpletree.binarytree import BinaryTree

  numero = [5,6,7,4,3,6,8]

  tree = BinaryTree()

  for e in range(0,len(numero)):
      tree.inserir_chave(numero[e])

  tree.em_ordem(tree.raiz)

  dado = tree.buscar_elemento(7)
  if dado != None:
      print("Elemento encontrado: " + str(dado.chave))
  else:
      print("Elemento não encontrado!")

  tree.remover_chave(3)
  tree.remover_chave(7)
  tree.em_ordem(tree.raiz)

  tree.salvar_arvore_no_arquivo(tree.raiz, "C:/Users/joaoc/Documents/Projetos", "arvore_arquivo")
