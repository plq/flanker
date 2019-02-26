
# mailbox_parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'mailboxAT ATOM COMMA CTEXT DOT DOT_ATOM DQUOTE DTEXT FWSP LANGLE LBRACKET LPAREN QPAIR QTEXT RANGLE RBRACKET RPAREN SEMICOLON URLmailbox_or_url_list : mailbox_or_url_list delim mailbox_or_url\n                           | mailbox_or_url_list delim\n                           | mailbox_or_urldelim : delim fwsp COMMA\n             | delim fwsp SEMICOLON\n             | COMMA\n             | SEMICOLONmailbox_or_url : mailbox\n                      | urlurl : ofwsp URL ofwspmailbox : addr_spec\n               | angle_addr\n               | name_addrname_addr : ofwsp phrase angle_addrangle_addr : ofwsp LANGLE addr_spec RANGLE ofwspaddr_spec : ofwsp local_part AT domain ofwsplocal_part : DOT_ATOM\n                  | ATOM\n                  | quoted_stringdomain : DOT_ATOM\n              | ATOM\n              | domain_literalquoted_string : DQUOTE quoted_string_text DQUOTE\n                     | DQUOTE DQUOTEquoted_string_text : quoted_string_text QTEXT\n                          | quoted_string_text QPAIR\n                          | quoted_string_text fwsp\n                          | QTEXT\n                          | QPAIR\n                          | fwspdomain_literal : LBRACKET domain_literal_text RBRACKET\n                      | LBRACKET RBRACKETdomain_literal_text : domain_literal_text DTEXT\n                           | domain_literal_text fwsp\n                           | DTEXT\n                           | fwspcomment : LPAREN comment_text RPAREN\n               | LPAREN RPARENcomment_text : comment_text CTEXT\n                    | comment_text fwsp\n                    | CTEXT\n                    | fwspphrase : phrase fwsp ATOM\n              | phrase fwsp DOT_ATOM\n              | phrase fwsp DOT\n              | phrase fwsp quoted_string\n              | phrase ATOM\n              | phrase DOT_ATOM\n              | phrase DOT\n              | phrase quoted_string\n              | ATOM\n              | DOT_ATOM\n              | DOT\n              | quoted_stringofwsp : fwsp comment fwsp\n             | fwsp comment\n             | comment fwsp\n             | comment\n             | fwsp\n             |fwsp : FWSP'
    
_lr_action_items = {'FWSP':([0,2,6,9,10,12,14,15,16,17,18,19,20,21,22,23,28,29,30,31,32,36,37,38,39,40,41,42,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,63,64,65,66,67,68,],[6,6,-61,6,6,6,-51,6,-52,6,-54,-53,-42,6,-38,-41,-30,-29,-28,-24,6,-48,-47,-50,-49,-40,-37,-39,6,6,6,-20,-21,-22,-27,-26,-25,-23,-44,-43,-46,-45,-36,-35,6,-32,-34,-33,-31,]),'LANGLE':([0,1,2,4,6,10,11,14,16,17,18,19,22,24,31,33,34,36,37,38,39,41,55,56,57,58,59,],[-60,-59,-58,12,-61,-56,-57,-51,-52,-60,-54,-53,-38,-55,-24,-59,12,-48,-47,-50,-49,-37,-23,-44,-43,-46,-45,]),'RPAREN':([6,9,20,21,23,40,42,],[-61,22,-42,41,-41,-40,-39,]),'QTEXT':([6,15,28,29,30,32,52,53,54,],[-61,30,-30,-29,-28,54,-27,-26,-25,]),'DTEXT':([6,48,62,63,64,66,67,],[-61,63,-36,-35,67,-34,-33,]),'DQUOTE':([0,1,2,4,6,10,11,12,14,15,16,17,18,19,22,24,25,28,29,30,31,32,33,36,37,38,39,41,52,53,54,55,56,57,58,59,],[-60,-59,-58,15,-61,-56,-57,-60,-51,31,-52,15,-54,-53,-38,-55,15,-30,-29,-28,-24,55,15,-48,-47,-50,-49,-37,-27,-26,-25,-23,-44,-43,-46,-45,]),'LBRACKET':([27,],[48,]),'QPAIR':([6,15,28,29,30,32,52,53,54,],[-61,29,-30,-29,-28,53,-27,-26,-25,]),'DOT_ATOM':([0,1,2,4,6,10,11,12,14,16,17,18,19,22,24,25,27,31,33,36,37,38,39,41,55,56,57,58,59,],[-60,-59,-58,16,-61,-56,-57,-60,-51,-52,36,-54,-53,-38,-55,43,49,-24,56,-48,-47,-50,-49,-37,-23,-44,-43,-46,-45,]),'AT':([13,14,16,18,31,43,44,45,55,],[27,-18,-17,-19,-24,-17,-18,-19,-23,]),'LPAREN':([0,1,6,12,14,16,17,18,19,31,33,36,37,38,39,46,47,49,50,51,55,56,57,58,59,65,68,],[9,9,-61,9,-51,-52,9,-54,-53,-24,9,-48,-47,-50,-49,9,9,-20,-21,-22,-23,-44,-43,-46,-45,-32,-31,]),'ATOM':([0,1,2,4,6,10,11,12,14,16,17,18,19,22,24,25,27,31,33,36,37,38,39,41,55,56,57,58,59,],[-60,-59,-58,14,-61,-56,-57,-60,-51,-52,37,-54,-53,-38,-55,44,50,-24,57,-48,-47,-50,-49,-37,-23,-44,-43,-46,-45,]),'RANGLE':([1,2,6,10,11,22,24,26,41,47,49,50,51,61,65,68,],[-59,-58,-61,-56,-57,-38,-55,46,-37,-60,-20,-21,-22,-16,-32,-31,]),'RBRACKET':([6,48,62,63,64,66,67,],[-61,65,-36,-35,68,-34,-33,]),'CTEXT':([6,9,20,21,23,40,42,],[-61,23,-42,42,-41,-40,-39,]),'DOT':([0,1,2,4,6,10,11,14,16,17,18,19,22,24,31,33,36,37,38,39,41,55,56,57,58,59,],[-60,-59,-58,19,-61,-56,-57,-51,-52,39,-54,-53,-38,-55,-24,59,-48,-47,-50,-49,-37,-23,-44,-43,-46,-45,]),'$end':([1,2,3,5,6,7,8,10,11,22,24,35,41,46,47,49,50,51,60,61,65,68,],[-59,-58,-13,-12,-61,0,-11,-56,-57,-38,-55,-14,-37,-60,-60,-20,-21,-22,-15,-16,-32,-31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'fwsp':([0,2,9,10,12,15,17,21,32,46,47,48,64,],[1,11,20,24,1,28,33,40,52,1,1,62,66,]),'comment':([0,1,12,17,33,46,47,],[2,10,2,2,10,2,2,]),'domain':([27,],[47,]),'comment_text':([9,],[21,]),'name_addr':([0,],[3,]),'ofwsp':([0,12,17,46,47,],[4,25,34,60,61,]),'angle_addr':([0,17,],[5,35,]),'local_part':([4,25,],[13,13,]),'mailbox':([0,],[7,]),'quoted_string_text':([15,],[32,]),'domain_literal_text':([48,],[64,]),'addr_spec':([0,12,],[8,26,]),'phrase':([4,],[17,]),'quoted_string':([4,17,25,33,],[18,38,45,58,]),'domain_literal':([27,],[51,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> mailbox","S'",1,None,None,None),
  ('mailbox_or_url_list -> mailbox_or_url_list delim mailbox_or_url','mailbox_or_url_list',3,'p_expression_mailbox_or_url_list','parser.py',19),
  ('mailbox_or_url_list -> mailbox_or_url_list delim','mailbox_or_url_list',2,'p_expression_mailbox_or_url_list','parser.py',20),
  ('mailbox_or_url_list -> mailbox_or_url','mailbox_or_url_list',1,'p_expression_mailbox_or_url_list','parser.py',21),
  ('delim -> delim fwsp COMMA','delim',3,'p_delim','parser.py',30),
  ('delim -> delim fwsp SEMICOLON','delim',3,'p_delim','parser.py',31),
  ('delim -> COMMA','delim',1,'p_delim','parser.py',32),
  ('delim -> SEMICOLON','delim',1,'p_delim','parser.py',33),
  ('mailbox_or_url -> mailbox','mailbox_or_url',1,'p_expression_mailbox_or_url','parser.py',36),
  ('mailbox_or_url -> url','mailbox_or_url',1,'p_expression_mailbox_or_url','parser.py',37),
  ('url -> ofwsp URL ofwsp','url',3,'p_expression_url','parser.py',41),
  ('mailbox -> addr_spec','mailbox',1,'p_expression_mailbox','parser.py',45),
  ('mailbox -> angle_addr','mailbox',1,'p_expression_mailbox','parser.py',46),
  ('mailbox -> name_addr','mailbox',1,'p_expression_mailbox','parser.py',47),
  ('name_addr -> ofwsp phrase angle_addr','name_addr',3,'p_expression_name_addr','parser.py',51),
  ('angle_addr -> ofwsp LANGLE addr_spec RANGLE ofwsp','angle_addr',5,'p_expression_angle_addr','parser.py',55),
  ('addr_spec -> ofwsp local_part AT domain ofwsp','addr_spec',5,'p_expression_addr_spec','parser.py',59),
  ('local_part -> DOT_ATOM','local_part',1,'p_expression_local_part','parser.py',63),
  ('local_part -> ATOM','local_part',1,'p_expression_local_part','parser.py',64),
  ('local_part -> quoted_string','local_part',1,'p_expression_local_part','parser.py',65),
  ('domain -> DOT_ATOM','domain',1,'p_expression_domain','parser.py',69),
  ('domain -> ATOM','domain',1,'p_expression_domain','parser.py',70),
  ('domain -> domain_literal','domain',1,'p_expression_domain','parser.py',71),
  ('quoted_string -> DQUOTE quoted_string_text DQUOTE','quoted_string',3,'p_expression_quoted_string','parser.py',75),
  ('quoted_string -> DQUOTE DQUOTE','quoted_string',2,'p_expression_quoted_string','parser.py',76),
  ('quoted_string_text -> quoted_string_text QTEXT','quoted_string_text',2,'p_expression_quoted_string_text','parser.py',83),
  ('quoted_string_text -> quoted_string_text QPAIR','quoted_string_text',2,'p_expression_quoted_string_text','parser.py',84),
  ('quoted_string_text -> quoted_string_text fwsp','quoted_string_text',2,'p_expression_quoted_string_text','parser.py',85),
  ('quoted_string_text -> QTEXT','quoted_string_text',1,'p_expression_quoted_string_text','parser.py',86),
  ('quoted_string_text -> QPAIR','quoted_string_text',1,'p_expression_quoted_string_text','parser.py',87),
  ('quoted_string_text -> fwsp','quoted_string_text',1,'p_expression_quoted_string_text','parser.py',88),
  ('domain_literal -> LBRACKET domain_literal_text RBRACKET','domain_literal',3,'p_expression_domain_literal','parser.py',92),
  ('domain_literal -> LBRACKET RBRACKET','domain_literal',2,'p_expression_domain_literal','parser.py',93),
  ('domain_literal_text -> domain_literal_text DTEXT','domain_literal_text',2,'p_expression_domain_literal_text','parser.py',100),
  ('domain_literal_text -> domain_literal_text fwsp','domain_literal_text',2,'p_expression_domain_literal_text','parser.py',101),
  ('domain_literal_text -> DTEXT','domain_literal_text',1,'p_expression_domain_literal_text','parser.py',102),
  ('domain_literal_text -> fwsp','domain_literal_text',1,'p_expression_domain_literal_text','parser.py',103),
  ('comment -> LPAREN comment_text RPAREN','comment',3,'p_expression_comment','parser.py',107),
  ('comment -> LPAREN RPAREN','comment',2,'p_expression_comment','parser.py',108),
  ('comment_text -> comment_text CTEXT','comment_text',2,'p_expression_comment_text','parser.py',112),
  ('comment_text -> comment_text fwsp','comment_text',2,'p_expression_comment_text','parser.py',113),
  ('comment_text -> CTEXT','comment_text',1,'p_expression_comment_text','parser.py',114),
  ('comment_text -> fwsp','comment_text',1,'p_expression_comment_text','parser.py',115),
  ('phrase -> phrase fwsp ATOM','phrase',3,'p_expression_phrase','parser.py',119),
  ('phrase -> phrase fwsp DOT_ATOM','phrase',3,'p_expression_phrase','parser.py',120),
  ('phrase -> phrase fwsp DOT','phrase',3,'p_expression_phrase','parser.py',121),
  ('phrase -> phrase fwsp quoted_string','phrase',3,'p_expression_phrase','parser.py',122),
  ('phrase -> phrase ATOM','phrase',2,'p_expression_phrase','parser.py',123),
  ('phrase -> phrase DOT_ATOM','phrase',2,'p_expression_phrase','parser.py',124),
  ('phrase -> phrase DOT','phrase',2,'p_expression_phrase','parser.py',125),
  ('phrase -> phrase quoted_string','phrase',2,'p_expression_phrase','parser.py',126),
  ('phrase -> ATOM','phrase',1,'p_expression_phrase','parser.py',127),
  ('phrase -> DOT_ATOM','phrase',1,'p_expression_phrase','parser.py',128),
  ('phrase -> DOT','phrase',1,'p_expression_phrase','parser.py',129),
  ('phrase -> quoted_string','phrase',1,'p_expression_phrase','parser.py',130),
  ('ofwsp -> fwsp comment fwsp','ofwsp',3,'p_expression_ofwsp','parser.py',139),
  ('ofwsp -> fwsp comment','ofwsp',2,'p_expression_ofwsp','parser.py',140),
  ('ofwsp -> comment fwsp','ofwsp',2,'p_expression_ofwsp','parser.py',141),
  ('ofwsp -> comment','ofwsp',1,'p_expression_ofwsp','parser.py',142),
  ('ofwsp -> fwsp','ofwsp',1,'p_expression_ofwsp','parser.py',143),
  ('ofwsp -> <empty>','ofwsp',0,'p_expression_ofwsp','parser.py',144),
  ('fwsp -> FWSP','fwsp',1,'p_expression_fwsp','parser.py',148),
]
