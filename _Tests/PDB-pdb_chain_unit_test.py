import unittest
from Chemistry.PDB.pdb_chain import *


class Test_pdb_chain(unittest.TestCase):
    def setUp(self):
        self.pdb_lines = [
            'ATOM      1  N   GLY     1      -1.105  -0.267  -0.062  1.00  0.00           N1+',
            'ATOM      2  CA  GLY     1       0.112   0.550   0.170  1.00  0.00           C',
            'ATOM      3  C   GLY     1       1.240  -0.152  -0.119  1.00  0.00           C',
            'ATOM      4  O   GLY     1       1.176  -1.323  -0.522  1.00  0.00           O',
            'ATOM      5  H1  GLY     1      -0.933  -1.171   0.368  1.00  0.00           H',
            'ATOM      6  H2  GLY     1      -1.222  -0.423  -1.054  1.00  0.00           H',
            'ATOM      7  H3  GLY     1      -1.924   0.172   0.330  1.00  0.00           H',
            'ATOM      8  HA2 GLY     1       0.107   1.445  -0.451  1.00  0.00           H',
            'ATOM      9  HA3 GLY     1       0.177   0.840   1.228  1.00  0.00           H',
            'ATOM     10  N   GLY     2       2.371   0.492   0.057  1.00  0.00           N',
            'ATOM     11  CA  GLY     2       3.674  -0.160  -0.222  1.00  0.00           C',
            'ATOM     12  C   GLY     2       4.711   0.684   0.027  1.00  0.00           C',
            'ATOM     13  O   GLY     2       4.510   1.838   0.434  1.00  0.00           O',
            'ATOM     14  H   GLY     2       2.354   1.437   0.384  1.00  0.00           H',
            'ATOM     15  HA2 GLY     2       3.809  -1.056   0.397  1.00  0.00           H',
            'ATOM     16  HA3 GLY     2       3.738  -0.441  -1.272  1.00  0.00           H',
            'ATOM     17  N   GLY     3       5.910   0.193  -0.192  1.00  0.00           N',
            'ATOM     18  CA  GLY     3       7.126   1.010   0.050  1.00  0.00           C',
            'ATOM     19  C   GLY     3       8.254   0.308  -0.249  1.00  0.00           C',
            'ATOM     20  O   GLY     3       8.691   0.305  -1.375  1.00  0.00           O',
            'ATOM     21  OXT GLY     3       8.839  -0.334   0.651  1.00  0.00           O1-',
            'ATOM     22  H   GLY     3       6.005  -0.747  -0.522  1.00  0.00           H',
            'ATOM     23  HA2 GLY     3       7.122   1.905  -0.581  1.00  0.00           H',
            'ATOM     24  HA3 GLY     3       7.191   1.300   1.088  1.00  0.00           H',
        ]
        self.ter_line = 'TER      25      GLY     3 '

    # ATOM     24  HA3 GLY     3       7.191   1.300   1.088  1.00  0.00           H
    # TER      25      GLY     3
    # TER      25  GLY

    def test_pdb_chain(self):
        chain = pdb_chain.from_pdb_atoms_lines(self.pdb_lines, self.ter_line)
        self.assertTrue(chain[0].pdb_line == self.pdb_lines[0])
        self.assertTrue(len(chain) == len(self.pdb_lines))

    def test_pdb_create_ter_line(self):
        ter_line = pdb_chain.create_ter_line(self.pdb_lines[-1])
        self.assertEqual(ter_line, self.ter_line)


class Test_pdb_chain_utils(unittest.TestCase):
    def setUp(self):
        self.pdb_lines = [
            'ATOM      1  N   GLY     1      -1.105  -0.267  -0.062  1.00  0.00           N1+',
            'ATOM      2  CA  GLY     1       0.112   0.550   0.170  1.00  0.00           C',
            'ATOM      3  C   GLY     1       1.240  -0.152  -0.119  1.00  0.00           C',
            'ATOM      4  O   GLY     1       1.176  -1.323  -0.522  1.00  0.00           O',
            'ATOM      5  H1  GLY     1      -0.933  -1.171   0.368  1.00  0.00           H',
            'ATOM      6  H2  GLY     1      -1.222  -0.423  -1.054  1.00  0.00           H',
            'ATOM      7  H3  GLY     1      -1.924   0.172   0.330  1.00  0.00           H',
            'ATOM      8  HA2 GLY     1       0.107   1.445  -0.451  1.00  0.00           H',
            'ATOM      9  HA3 GLY     1       0.177   0.840   1.228  1.00  0.00           H',
            'ATOM     10  N   GLY     2       2.371   0.492   0.057  1.00  0.00           N',
            'ATOM     11  CA  GLY     2       3.674  -0.160  -0.222  1.00  0.00           C',
            'ATOM     12  C   GLY     2       4.711   0.684   0.027  1.00  0.00           C',
            'ATOM     13  O   GLY     2       4.510   1.838   0.434  1.00  0.00           O',
            'ATOM     14  H   GLY     2       2.354   1.437   0.384  1.00  0.00           H',
            'ATOM     15  HA2 GLY     2       3.809  -1.056   0.397  1.00  0.00           H',
            'ATOM     16  HA3 GLY     2       3.738  -0.441  -1.272  1.00  0.00           H',
            'ATOM     17  N   GLY     3       5.910   0.193  -0.192  1.00  0.00           N',
            'ATOM     18  CA  GLY     3       7.126   1.010   0.050  1.00  0.00           C',
            'ATOM     19  C   GLY     3       8.254   0.308  -0.249  1.00  0.00           C',
            'ATOM     20  O   GLY     3       8.691   0.305  -1.375  1.00  0.00           O',
            'ATOM     21  OXT GLY     3       8.839  -0.334   0.651  1.00  0.00           O1-',
            'ATOM     22  H   GLY     3       6.005  -0.747  -0.522  1.00  0.00           H',
            'ATOM     23  HA2 GLY     3       7.122   1.905  -0.581  1.00  0.00           H',
            'ATOM     24  HA3 GLY     3       7.191   1.300   1.088  1.00  0.00           H',
        ]
        self.ter_line = 'TER      25      GLY     3 '
        chain = pdb_chain.from_pdb_atoms_lines(self.pdb_lines, self.ter_line)

    def test_chain2residues_list(self):
        chain = pdb_chain.from_pdb_atoms_lines(self.pdb_lines, self.ter_line)
        chain_util = chain_utils(chain)
        residues = chain_util.chain2residues_list()
        self.assertEqual(len(residues), 3)
        res_names = list(map(lambda r: r.resname, residues))
        self.assertEqual(res_names, ['GLY', 'GLY', 'GLY'])
        res_seqs = list(map(lambda r: r.resseq, residues))
        self.assertEqual(res_seqs, [1, 2, 3])

    def test_remove_residues(self):
        chain = pdb_chain.from_pdb_atoms_lines(self.pdb_lines, self.ter_line)
        chain_util = chain_utils(chain)
        new_chain = chain_util.remove_residues_by_resseqs([2])
        residues = chain_utils(new_chain).chain2residues_list()
        self.assertEqual(len(residues), 2)
        res_names = list(map(lambda r: r.resname, residues))
        self.assertEqual(res_names, ['GLY', 'GLY'])
        res_seqs = list(map(lambda r: r.resseq, residues))
        self.assertEqual(res_seqs, [1, 3])
