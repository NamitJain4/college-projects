----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 27.08.2024 14:32:46
-- Design Name: 
-- Module Name: digital_display - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity digital_display is
    Port ( 
        p : in STD_LOGIC;
        q : in STD_LOGIC;
        r : in STD_LOGIC;
        s : in STD_LOGIC;
        A : out STD_LOGIC;
        B : out STD_LOGIC;
        C : out STD_LOGIC;
        D : out STD_LOGIC;
        E : out STD_LOGIC;
        F : out STD_LOGIC;
        G : out STD_LOGIC
    );
end digital_display;

architecture Behavioral of digital_display is

begin
    A <= not((not p and not q and not r and not s) or (not p and q and not r and s) or (p and not r and not s) or (p and not q and not r) or (not p and not q and r) or (q and r) or (p and not q and r and not s));
    B <= not((not q and not r) or (not p and q and not r and not s) or (p and q and not r and s) or (not p and r and s) or (not q and r and not s));
    C <= not((p and not r and s) or (p and not q and r) or (not q and not r and not s) or (not p and q and not s) or (not p and s));
    D <= not((not q and not r and not s) or (p and not q and s) or (q and r and not s) or (not p and not q and r) or (q and not r and s) or (p and q and not r and not s));
    E <= not((not q and not r and not s) or (p and q and not r) or (not p and r and not s) or (p and r));
    F <= not((not r and not s) or (p and not q and not r and s) or (not p and q and not r and s) or (not p and q and r and not s) or (p and r));
    G <= not((not p and q and not r) or (p and not q and not r and not s) or (not p and not q and r and s) or (p and s) or (r and not s));

end Behavioral;
