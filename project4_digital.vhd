----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 03.09.2024 15:33:32
-- Design Name: 
-- Module Name: project4_digital - Behavioral
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
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity project4_digital is
    Port (
        clk_in : in STD_LOGIC;
        s1 : in STD_LOGIC;
        s2 : in STD_LOGIC;
        s3 : in STD_LOGIC;
        s4 : in STD_LOGIC;
        s5 : in STD_LOGIC;
        s6 : in STD_LOGIC;
        s7 : in STD_LOGIC;
        s8 : in STD_LOGIC;
        s9 : in STD_LOGIC;
        s10 : in STD_LOGIC;
        s11 : in STD_LOGIC;
        s12 : in STD_LOGIC;
        s13 : in STD_LOGIC;
        s14 : in STD_LOGIC;
        s15 : in STD_LOGIC;
        s16 : in STD_LOGIC;
        c1 : out STD_LOGIC := '0';
        c2 : out STD_LOGIC := '0';
        c3 : out STD_LOGIC := '0';
        c4 : out STD_LOGIC := '0';
        c5 : out STD_LOGIC := '0';
        c6 : out STD_LOGIC := '0';
        c7 : out STD_LOGIC := '0';
        anode_sel : out STD_LOGIC_VECTOR (3 downto 0) := "0000"
    );
end project4_digital;

architecture Behavioral of project4_digital is
    component Timing_block
        Port (
            clk_in : in STD_LOGIC; -- 100 MHz input clock
            mux_select : out STD_LOGIC_VECTOR (1 downto 0); -- Signal for the mux
            anodes : out STD_LOGIC_VECTOR (3 downto 0) -- Anodes signal for display
        );
    end component;
    
    component digital_display
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
    end component;
    
    component mux4x1_4bit
        Port (
            inp1 : in STD_LOGIC_VECTOR (3 downto 0);
            inp2 : in STD_LOGIC_VECTOR (3 downto 0);
            inp3 : in STD_LOGIC_VECTOR (3 downto 0);
            inp4 : in STD_LOGIC_VECTOR (3 downto 0);
            Sel : in STD_LOGIC_VECTOR (1 downto 0);
            output : out STD_LOGIC_VECTOR (3 downto 0)
        );
    end component;
    signal selector : STD_LOGIC_VECTOR (1 downto 0);
    signal curr_num : STD_LOGIC_VECTOR (3 downto 0);
    signal sw_set1 : STD_LOGIC_VECTOR (3 downto 0) := s1 & s2 & s3 & s4;
    signal sw_set2 : STD_LOGIC_VECTOR (3 downto 0) := s5 & s6 & s7 & s8;
    signal sw_set3 : STD_LOGIC_VECTOR (3 downto 0) := s9 & s10 & s11 & s12;
    signal sw_set4 : STD_LOGIC_VECTOR (3 downto 0) := s13 & s14 & s15 & s16;
begin
    sw_set1 <= s1 & s2 & s3 & s4;
    sw_set2 <= s5 & s6 & s7 & s8;
    sw_set3 <= s9 & s10 & s11 & s12;
    sw_set4 <= s13 & s14 & s15 & s16; 
    DUT1 : Timing_block port map (clk_in => clk_in, mux_select => selector, anodes => anode_sel);
    DUT2 : mux4x1_4bit port map (inp1 => sw_set1, inp2 => sw_set2, inp3 => sw_set3, inp4 => sw_set4, Sel => selector, output => curr_num);
    DUT3 : digital_display port map (p => curr_num(0), q => curr_num(1), r => curr_num(2), s => curr_num(3), A => c1, B => c2, C => c3, D => c4, E => c5, F => c6, G => c7);

end Behavioral;
